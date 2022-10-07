// File Name: ./files/Uni_HL_20221007_1058/ANdecoder_Uni_HL_29_tb_for_N_23234.v
// module= 29
// N= 23234

module ANdecoder_tb;
reg [27:0] ANe;
wire [22:0] Nc;

ANdecoder D0(ANe, Nc);
initial begin
$dumpfile("./files/Uni_HL_20221007_1058/A29N23234.vcd"); 
$dumpvars(0, ANdecoder_tb);

ANe=28'd0;

ANe=28'd673784; //R=27, error bit=1
#10 ANe=28'd673778; //R=21, error bit=3
#10 ANe=28'd673770; //R=13, error bit=4
#10 ANe=28'd673754; //R=26, error bit=5
#10 ANe=28'd673722; //R=23, error bit=6
#10 ANe=28'd673658; //R=17, error bit=7
#10 ANe=28'd673530; //R=5, error bit=8
#10 ANe=28'd673274; //R=10, error bit=9
#10 ANe=28'd672762; //R=20, error bit=10
#10 ANe=28'd657402; //R=1, error bit=14
#10 ANe=28'd542714; //R=8, error bit=17
#10 ANe=28'd149498; //R=3, error bit=19
#10 $finish;
end
endmodule
