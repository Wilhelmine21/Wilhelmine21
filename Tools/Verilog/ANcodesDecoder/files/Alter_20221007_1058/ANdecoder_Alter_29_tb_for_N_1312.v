// File Name: ./files/Alter_20221007_1058/ANdecoder_Alter_29_tb_for_N_1312.v
// module= 29
// N= 1312

module ANdecoder_tb;
reg [27:0] ANe;
wire [22:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/Alter_20221007_1058/A29N1312.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=28'd38049; //R=1, error bit=0
#10 ANe=28'd38050; //R=2, error bit=1
#10 ANe=28'd38052; //R=4, error bit=2
#10 ANe=28'd38056; //R=8, error bit=3
#10 ANe=28'd38064; //R=16, error bit=4
#10 ANe=28'd38112; //R=6, error bit=6
#10 ANe=28'd38304; //R=24, error bit=8
#10 ANe=28'd38560; //R=19, error bit=9
#10 ANe=28'd40096; //R=18, error bit=11
#10 ANe=28'd46240; //R=14, error bit=13
#10 ANe=28'd54432; //R=28, error bit=14
#10 ANe=28'd103584; //R=25, error bit=16
#10 ANe=28'd169120; //R=21, error bit=17
#10 ANe=28'd300192; //R=13, error bit=18
#10 ANe=28'd562336; //R=26, error bit=19
#10 ANe=28'd1086624; //R=23, error bit=20
#10 ANe=28'd2135200; //R=17, error bit=21
#10 ANe=28'd4232352; //R=5, error bit=22
#10 ANe=28'd8426656; //R=10, error bit=23
#10 ANe=28'd16815264; //R=20, error bit=24
#10 ANe=28'd33592480; //R=11, error bit=25
#10 ANe=28'd67146912; //R=22, error bit=26
#10 ANe=28'd134255776; //R=15, error bit=27
#10 ANe=28'd38016; //R=26, error bit=5
#10 ANe=28'd37920; //R=17, error bit=7
#10 ANe=28'd37024; //R=20, error bit=10
#10 ANe=28'd33952; //R=22, error bit=12
#10 ANe=28'd5280; //R=2, error bit=15
#10 $finish;
end
endmodule
