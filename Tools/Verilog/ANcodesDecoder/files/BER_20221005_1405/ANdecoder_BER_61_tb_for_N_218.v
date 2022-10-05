// File Name: ./files/BER_20221005_1405/ANdecoder_BER_61_tb_for_N_218.v
// module= 61
// N= 218

module ANdecoder_tb;
reg [29:0] numX;
wire [23:0] out;

ANdecoder D0(numX, out);
initial begin
$dumpfile("./files/BER_20221005_1405/A61N218.vcd"); 
$dumpvars(0, ANdecoder_tb);

numX=30'd0;

#10 numX=30'd78834;
#10 numX=30'd33567730;
#10 numX=30'd13042;
#10 numX=30'd13296;
#10 numX=30'd536884210;
#10 $finish;
end
endmodule
