// File Name: ./files/Uni_HL_20221007_1058/ANdecoder_Uni_HL_29_for_N_23234.v
// module= 29
// 可更正AN的bit數= 28
// mod的bit數= 5
// 可更正N的bit數= 23

module ANdecoder(ANe, Nc);
input [27:0] ANe;
output [22:0] Nc;
wire [4:0] mod_tri;
wire [4:0] not_mod_tri;
wire [27:0] error_bit;
wire [27:0] ANc;
assign mod_tri = ANe % 29;

//not gate
not not_0(not_mod_tri[0], mod_tri[0]);
not not_1(not_mod_tri[1], mod_tri[1]);
not not_2(not_mod_tri[2], mod_tri[2]);
not not_3(not_mod_tri[3], mod_tri[3]);
not not_4(not_mod_tri[4], mod_tri[4]);
//and gate
and and_1(error_bit[14], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_2(error_bit[15], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_3(error_bit[19], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_4(error_bit[16], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_5(error_bit[8], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_6(error_bit[20], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_7(error_bit[26], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_8(error_bit[17], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_9(error_bit[24], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_10(error_bit[9], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_11(error_bit[11], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_12(error_bit[21], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_13(error_bit[4], mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_14(error_bit[27], not_mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_15(error_bit[13], mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_16(error_bit[18], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_17(error_bit[7], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_18(error_bit[25], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_19(error_bit[23], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_20(error_bit[10], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_21(error_bit[3], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_22(error_bit[12], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_23(error_bit[6], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_24(error_bit[22], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and_25(error_bit[2], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and_26(error_bit[5], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and_27(error_bit[1], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and_28(error_bit[0], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], mod_tri[4]);
//or gate
or or_0(ANc[0],error_bit[0], ANe[0]);
or or_1(ANc[1],error_bit[1], ANe[1]);
or or_2(ANc[2],error_bit[2], ANe[2]);
or or_3(ANc[3],error_bit[3], ANe[3]);
or or_4(ANc[4],error_bit[4], ANe[4]);
or or_5(ANc[5],error_bit[5], ANe[5]);
or or_6(ANc[6],error_bit[6], ANe[6]);
or or_7(ANc[7],error_bit[7], ANe[7]);
or or_8(ANc[8],error_bit[8], ANe[8]);
or or_9(ANc[9],error_bit[9], ANe[9]);
or or_10(ANc[10],error_bit[10], ANe[10]);
or or_11(ANc[11],error_bit[11], ANe[11]);
or or_12(ANc[12],error_bit[12], ANe[12]);
or or_13(ANc[13],error_bit[13], ANe[13]);
or or_14(ANc[14],error_bit[14], ANe[14]);
or or_15(ANc[15],error_bit[15], ANe[15]);
or or_16(ANc[16],error_bit[16], ANe[16]);
or or_17(ANc[17],error_bit[17], ANe[17]);
or or_18(ANc[18],error_bit[18], ANe[18]);
or or_19(ANc[19],error_bit[19], ANe[19]);
or or_20(ANc[20],error_bit[20], ANe[20]);
or or_21(ANc[21],error_bit[21], ANe[21]);
or or_22(ANc[22],error_bit[22], ANe[22]);
or or_23(ANc[23],error_bit[23], ANe[23]);
or or_24(ANc[24],error_bit[24], ANe[24]);
or or_25(ANc[25],error_bit[25], ANe[25]);
or or_26(ANc[26],error_bit[26], ANe[26]);
or or_27(ANc[27],error_bit[27], ANe[27]);
assign Nc = ANc / 29;

endmodule