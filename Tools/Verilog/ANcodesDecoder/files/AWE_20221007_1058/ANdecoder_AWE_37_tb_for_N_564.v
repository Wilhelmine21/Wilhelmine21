// File Name: ./files/AWE_20221007_1058/ANdecoder_AWE_37_tb_for_N_564.v
// module= 37
// N= 564

module ANdecoder_tb;
reg [17:0] ANe;
wire [11:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/AWE_20221007_1058/A37N564.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=18'd0;

ANe=18'd20869; //R=1, error bit=0
#10 ANe=18'd20870; //R=2, error bit=1
#10 ANe=18'd20872; //R=4, error bit=2
#10 ANe=18'd20876; //R=8, error bit=3
#10 ANe=18'd20884; //R=16, error bit=4
#10 ANe=18'd20900; //R=32, error bit=5
#10 ANe=18'd20932; //R=27, error bit=6
#10 ANe=18'd20996; //R=17, error bit=7
#10 ANe=18'd21124; //R=34, error bit=8
#10 ANe=18'd21380; //R=31, error bit=9
#10 ANe=18'd21892; //R=25, error bit=10
#10 ANe=18'd22916; //R=13, error bit=11
#10 ANe=18'd24964; //R=26, error bit=12
#10 ANe=18'd29060; //R=15, error bit=13
#10 ANe=18'd37252; //R=30, error bit=14
#10 ANe=18'd53636; //R=23, error bit=15
#10 ANe=18'd86404; //R=9, error bit=16
#10 ANe=18'd151940; //R=18, error bit=17
#10 ANe=18'd20867; //R=36, error bit=0
#10 ANe=18'd20866; //R=35, error bit=1
#10 ANe=18'd20864; //R=33, error bit=2
#10 ANe=18'd20860; //R=29, error bit=3
#10 ANe=18'd20852; //R=21, error bit=4
#10 ANe=18'd20836; //R=5, error bit=5
#10 ANe=18'd20804; //R=10, error bit=6
#10 ANe=18'd20740; //R=20, error bit=7
#10 ANe=18'd20612; //R=3, error bit=8
#10 ANe=18'd20356; //R=6, error bit=9
#10 ANe=18'd19844; //R=12, error bit=10
#10 ANe=18'd18820; //R=24, error bit=11
#10 ANe=18'd16772; //R=11, error bit=12
#10 ANe=18'd12676; //R=22, error bit=13
#10 ANe=18'd4484; //R=7, error bit=14
//ANe=-11900(­t¼Æ), R=14, error bit=15
//ANe=-44668(­t¼Æ), R=28, error bit=16
//ANe=-110204(­t¼Æ), R=19, error bit=17
#10 $finish;
end
endmodule
