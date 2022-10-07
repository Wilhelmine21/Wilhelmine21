// File Name: ./files/BER_20221007_1022/ANdecoder_BER_47_tb_for_N_1213.v
// module= 47
// N= 1213

module ANdecoder_tb;
reg [22:0] ANe;
wire [16:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/BER_20221007_1022/A47N1213.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=23'd57015; //R=4, error bit=2
#10 ANe=23'd57019; //R=8, error bit=3
#10 ANe=23'd57075; //R=17, error bit=6
#10 ANe=23'd57267; //R=21, error bit=8
#10 ANe=23'd65203; //R=14, error bit=13
#10 ANe=23'd122547; //R=18, error bit=16
#10 ANe=23'd188083; //R=36, error bit=17
#10 ANe=23'd319155; //R=25, error bit=18
#10 ANe=23'd581299; //R=3, error bit=19
#10 ANe=23'd1105587; //R=6, error bit=20
#10 ANe=23'd2154163; //R=12, error bit=21
#10 ANe=23'd4251315; //R=24, error bit=22
#10 ANe=23'd57010; //R=46, error bit=0
#10 ANe=23'd57009; //R=45, error bit=1
#10 ANe=23'd56995; //R=31, error bit=4
#10 ANe=23'd56979; //R=15, error bit=5
#10 ANe=23'd56883; //R=13, error bit=7
#10 ANe=23'd56499; //R=5, error bit=9
#10 ANe=23'd55987; //R=10, error bit=10
#10 ANe=23'd54963; //R=20, error bit=11
#10 ANe=23'd52915; //R=40, error bit=12
#10 ANe=23'd40627; //R=19, error bit=14
#10 ANe=23'd24243; //R=38, error bit=15
#10 $finish;
end
endmodule
