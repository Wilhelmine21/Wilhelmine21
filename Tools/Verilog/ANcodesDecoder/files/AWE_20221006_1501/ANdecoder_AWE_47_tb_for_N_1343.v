// File Name: ./files/AWE_20221006_1501/ANdecoder_AWE_47_tb_for_N_1343.v
// module= 47
// N= 1343

module ANdecoder_tb;
reg [22:0] numX;
wire [16:0] out;

ANdecoder D0(numX, out);
initial begin
$dumpfile("./files/AWE_20221006_1501/A47N1343.vcd"); 
$dumpvars(0, ANdecoder_tb);

numX=23'd0;

numX=23'd63122; //R=1, error bit=0
#10 numX=23'd63123; //R=2, error bit=1
#10 numX=23'd63125; //R=4, error bit=2
#10 numX=23'd63129; //R=8, error bit=3
#10 numX=23'd63137; //R=16, error bit=4
#10 numX=23'd63153; //R=32, error bit=5
#10 numX=23'd63185; //R=17, error bit=6
#10 numX=23'd63249; //R=34, error bit=7
#10 numX=23'd63377; //R=21, error bit=8
#10 numX=23'd63633; //R=42, error bit=9
#10 numX=23'd64145; //R=37, error bit=10
#10 numX=23'd65169; //R=27, error bit=11
#10 numX=23'd67217; //R=7, error bit=12
#10 numX=23'd71313; //R=14, error bit=13
#10 numX=23'd79505; //R=28, error bit=14
#10 numX=23'd95889; //R=9, error bit=15
#10 numX=23'd128657; //R=18, error bit=16
#10 numX=23'd194193; //R=36, error bit=17
#10 numX=23'd325265; //R=25, error bit=18
#10 numX=23'd587409; //R=3, error bit=19
#10 numX=23'd1111697; //R=6, error bit=20
#10 numX=23'd2160273; //R=12, error bit=21
#10 numX=23'd4257425; //R=24, error bit=22
#10 numX=23'd63120; //R=46, error bit=0
#10 numX=23'd63119; //R=45, error bit=1
#10 numX=23'd63117; //R=43, error bit=2
#10 numX=23'd63113; //R=39, error bit=3
#10 numX=23'd63105; //R=31, error bit=4
#10 numX=23'd63089; //R=15, error bit=5
#10 numX=23'd63057; //R=30, error bit=6
#10 numX=23'd62993; //R=13, error bit=7
#10 numX=23'd62865; //R=26, error bit=8
#10 numX=23'd62609; //R=5, error bit=9
#10 numX=23'd62097; //R=10, error bit=10
#10 numX=23'd61073; //R=20, error bit=11
#10 numX=23'd59025; //R=40, error bit=12
#10 numX=23'd54929; //R=33, error bit=13
#10 numX=23'd46737; //R=19, error bit=14
#10 numX=23'd30353; //R=38, error bit=15
//ANe=-2415(璽计), R=29, error bit=16
//ANe=-67951(璽计), R=11, error bit=17
//ANe=-199023(璽计), R=22, error bit=18
//ANe=-461167(璽计), R=44, error bit=19
//ANe=-985455(璽计), R=41, error bit=20
//ANe=-2034031(璽计), R=35, error bit=21
//ANe=-4131183(璽计), R=23, error bit=22
#10 $finish;
end
endmodule
