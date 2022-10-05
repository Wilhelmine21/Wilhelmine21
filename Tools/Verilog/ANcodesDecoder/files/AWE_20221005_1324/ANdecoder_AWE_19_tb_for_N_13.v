// File Name: ./files/AWE_20221005_1324/ANdecoder_AWE_19_tb_for_N_13.v
// module= 19
// N= 13

module ANdecoder_tb;
reg [8:0] numX;
wire [3:0] out;

ANdecoder D0(numX, out);
initial begin
$dumpfile("./files/AWE_20221005_1324/A19N13.vcd"); 
$dumpvars(0, ANdecoder_tb);

numX=9'd0;
#10 numX=9'd215;
#10 numX=9'd245;
#10 numX=9'd255;
#10 numX=9'd243;
#10 numX=9'd183;

#10 $finish;
end
endmodule
