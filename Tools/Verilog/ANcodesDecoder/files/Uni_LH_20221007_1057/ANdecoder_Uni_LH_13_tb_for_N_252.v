// File Name: ./files/Uni_LH_20221007_1057/ANdecoder_Uni_LH_13_tb_for_N_252.v
// module= 13
// N= 252

module ANdecoder_tb;
reg [11:0] ANe;
wire [7:0] Nc;

ANdecoder D0( ANe, Nc);
initial begin
$dumpfile("./files/Uni_LH_20221007_1057/A13N252.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=12'd0;

ANe=12'd3277; //R=1, error bit=0
#10 ANe=12'd3278; //R=2, error bit=1
#10 ANe=12'd3292; //R=3, error bit=4
#10 ANe=12'd3308; //R=6, error bit=5
#10 ANe=12'd3532; //R=9, error bit=8
#10 ANe=12'd3788; //R=5, error bit=9
#10 $finish;
end
endmodule
