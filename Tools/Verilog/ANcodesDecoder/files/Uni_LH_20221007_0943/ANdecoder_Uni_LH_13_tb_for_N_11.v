// File Name: ./files/Uni_LH_20221007_0943/ANdecoder_Uni_LH_13_tb_for_N_11.v
// module= 13
// N= 11

module ANdecoder_tb;
reg [11:0] ANe;
wire [7:0] Nc;

ANdecoder D0( ANe, Nc);
initial begin
$dumpfile("./files/Uni_LH_20221007_0943/A13N11.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=12'd0;

ANe=12'd159; //R=3, error bit=4
#10 ANe=12'd175; //R=6, error bit=5
#10 ANe=12'd207; //R=12, error bit=6
#10 ANe=12'd399; //R=9, error bit=8
#10 ANe=12'd655; //R=5, error bit=9
#10 ANe=12'd1167; //R=10, error bit=10
#10 ANe=12'd2191; //R=7, error bit=11
#10 $finish;
end
endmodule
