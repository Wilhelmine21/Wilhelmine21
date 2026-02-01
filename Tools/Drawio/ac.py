import sys
import os
import re

def trans_time(value, from_u, to_u):
    factors = {'s': 1.0, 'ms': 1e-3, 'us': 1e-6, 'ns': 1e-9, 'ps': 1e-12, 'fs': 1e-15}
    return value * factors[from_u.lower()] / factors[to_u.lower()]

def parse_timescale(time_scale):
    #extracts numeric factor and unit from strings like '10ps'
    match = re.match(r"(\d+)([a-z]+)", time_scale.lower())
    if not match: 
        raise ValueError(f"Invalid timescale format: {time_scale}")
    return int(match.group(1)), match.group(2)

# ==================================== #
if len(sys.argv) < 3:
    script_name=os.path.basename(sys.argv[0])
    print(f"Usage: {script_name} <time_scale> <clock_info_file>")
    sys.exit(1)

time_scale_input = sys.argv[1]
time_scale_factor, time_scale_unit = parse_timescale(time_scale_input)

fclk=sys.argv[2]
fout="str_out.list"
# ================ Read clock information from file ================ #
try:
    with open(fclk, 'r') as f:
        # Filter out empty lines and comments starting with '#'
        clk_data = [(line.split()[0], float(line.split()[1])) for line in f if line.strip() and "#" not in line]
except FileNotFoundError:
    print(f"Error: File {fclk} not found.")
    sys.exit(1)

# ================ Start to generate clock string ================ #
out, launch, capture = [], [], []
period_slow = 10
period_slow_scale = int(trans_time(period_slow, 'ns', time_scale_unit) / time_scale_factor)
out.append(f"// Info: slow period is {period_slow}ns = {period_slow_scale} *{time_scale_input}")
out.append(f"// Info: slow waveform is [{int(3*period_slow_scale/10)}, {int(5*period_slow_scale/10)}]\n")

print(f"--- Starting Conversion Verification (Base: {time_scale_input}) ---")

for clk_name, clk_period in clk_data:
    # Calculate scale value: (Value in ns converted to target unit) / time_scale factor
    clk_period_scale = trans_time(clk_period, 'ns', time_scale_unit) / time_scale_factor
    
    # --- Verification Logic ---
    # Revert back to ns: (scale_val * factor) converted from target unit to 'ns'
    reverted_ns = trans_time(clk_period_scale * time_scale_factor, time_scale_unit, 'ns')
    error = abs(clk_period - reverted_ns)
    status = "PASS" if error < 1e-7 else "FAIL"
    print(f"[{status}] {clk_name:15} | Org: {clk_period:>6}ns | Rev: {reverted_ns:>8.4f}ns | Err: {error:.2e}")
    
    # Generate strings for the output list
    info = f"// Info: {clk_name} is {clk_period}ns = {clk_period_scale:.2f} *{time_scale_input}"
    v_msg = f"// Verify: {clk_name} Reverted = {reverted_ns:.4f}ns [{status}]"
    
    # Launch Calculation
    lanch_w1, lanch_w2 = period_slow_scale - (clk_period_scale * 0.75), clk_period_scale / 2
    launch.extend([
        info, v_msg, 
        f"//\tlaunch w1 = {period_slow_scale} - ({clk_period_scale:.3f}*0.75) = {lanch_w1:.3f}", 
        f"//\tlanuch w2 = {clk_period_scale:.3f}/2 = {lanch_w2:.3f}", 
        f"pulse {clk_name} {lanch_w1:.0f} {lanch_w2:.0f};\n"
    ])
    
    # Capture Calculation
    capture_w1, capture_w2 = clk_period_scale / 4, clk_period_scale / 2
    capture.extend([
        info, v_msg, 
        f"//\tcapture w1 = {clk_period_scale:.3f}/4 = {capture_w1:.3f}", 
        f"//\tcapture w2 = {clk_period_scale:.3f}/2 = {capture_w2:.3f}", 
        f"pulse {clk_name} {capture_w1:.0f} {capture_w2:.0f};\n"
    ])
    
# ================ Write out data to file ================ #
with open(fout, 'w') as fw:
    fw.write("\n".join(out + launch + ["\n"] + capture))