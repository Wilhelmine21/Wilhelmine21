// File Name: ./files/Uni_HL_20221007_0944/ANdecoder_Uni_HL_13_tb_for_N_11.v
// module= 13
// N= 11

module ANdecoder_tb;
reg [11:0] ANe;
wire [7:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/Uni_HL_20221007_0944/A13N11.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=12'd0;

ANe=12'd142; //R=12, error bit=0
#10 ANe=12'd141; //R=11, error bit=1
#10 ANe=12'd139; //R=9, error bit=2
#10 ANe=12'd135; //R=5, error bit=3
#10 ANe=12'd15; //R=2, error bit=7
#10 $finish;
end
endmodule
