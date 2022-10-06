// File Name: ./files/BER_20221006_1611/ANdecoder_BER_19_tb_for_N_11.v
// module= 19
// N= 11

module ANdecoder_tb;
reg [8:0] ANe;
wire [3:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/BER_20221006_1611/A19N11.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=9'd211; //R=2, error bit=1
#10 ANe=9'd213; //R=4, error bit=2
#10 ANe=9'd217; //R=8, error bit=3
#10 ANe=9'd241; //R=13, error bit=5
#10 ANe=9'd465; //R=9, error bit=8
#10 ANe=9'd208; //R=18, error bit=0
#10 ANe=9'd193; //R=3, error bit=4
#10 ANe=9'd145; //R=12, error bit=6
#10 ANe=9'd81; //R=5, error bit=7
#10 $finish;
end
endmodule
