// File Name: ./files/BER_20221007_1058/ANdecoder_BER_29_tb_for_N_123.v
// module= 29
// N= 123

module ANdecoder_tb;
reg [13:0] ANe;
wire [8:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/BER_20221007_1058/A29N123.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=14'd3583; //R=16, error bit=4
#10 ANe=14'd4079; //R=19, error bit=9
#10 ANe=14'd7663; //R=7, error bit=12
#10 ANe=14'd11759; //R=14, error bit=13
#10 ANe=14'd3566; //R=28, error bit=0
#10 ANe=14'd3565; //R=27, error bit=1
#10 ANe=14'd3563; //R=25, error bit=2
#10 ANe=14'd3559; //R=21, error bit=3
#10 ANe=14'd3535; //R=26, error bit=5
#10 ANe=14'd3503; //R=23, error bit=6
#10 ANe=14'd3439; //R=17, error bit=7
#10 ANe=14'd3311; //R=5, error bit=8
#10 ANe=14'd2543; //R=20, error bit=10
#10 ANe=14'd1519; //R=11, error bit=11
#10 $finish;
end
endmodule
