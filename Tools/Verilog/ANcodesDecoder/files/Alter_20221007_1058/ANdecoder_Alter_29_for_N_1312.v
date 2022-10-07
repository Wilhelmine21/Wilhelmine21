// File Name: ./files/Alter_20221007_1058/ANdecoder_Alter_29_for_N_1312.v
// module= 29
// 可更正AN的bit數= 28
// mod的bit數= 5
// 可更正N的bit數= 23

module ANdecoder(ANe, Nc);
input [27:0] ANe;
output [22:0] Nc;
wire [4:0] mod_tri;
wire [4:0] not_mod_tri;
wire [27:0] R;
wire [27:0] notR;
wire [27:0] ANc1;
wire [27:0] ANc2;
wire [4:0] check;
wire [27:0] ANc;

assign mod_tri = ANe % 29;

//not0 gate
not not0_0(not_mod_tri[0], mod_tri[0]);
not not0_1(not_mod_tri[1], mod_tri[1]);
not not0_2(not_mod_tri[2], mod_tri[2]);
not not0_3(not_mod_tri[3], mod_tri[3]);
not not0_4(not_mod_tri[4], mod_tri[4]);
//and gate
and and0_1(R[0], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_2(R[1], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_3(R[2], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_4(R[3], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_5(R[4], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_6(R[5], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_7(R[6], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and0_8(R[7], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_9(R[8], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_10(R[9], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_11(R[10], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_12(R[11], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_13(R[12], mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_14(R[13], not_mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_15(R[14], mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and0_16(R[15], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_17(R[16], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_18(R[17], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_19(R[18], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_20(R[19], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_21(R[20], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_22(R[21], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_23(R[22], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and0_24(R[23], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and0_25(R[24], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and0_26(R[25], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and0_27(R[26], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4]);
and and0_28(R[27], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], mod_tri[4]);
//not1 gate
not not1_0(notR[0], R[0]);
not not1_1(notR[1], R[1]);
not not1_2(notR[2], R[2]);
not not1_3(notR[3], R[3]);
not not1_4(notR[4], R[4]);
not not1_5(notR[5], R[5]);
not not1_6(notR[6], R[6]);
not not1_7(notR[7], R[7]);
not not1_8(notR[8], R[8]);
not not1_9(notR[9], R[9]);
not not1_10(notR[10], R[10]);
not not1_11(notR[11], R[11]);
not not1_12(notR[12], R[12]);
not not1_13(notR[13], R[13]);
not not1_14(notR[14], R[14]);
not not1_15(notR[15], R[15]);
not not1_16(notR[16], R[16]);
not not1_17(notR[17], R[17]);
not not1_18(notR[18], R[18]);
not not1_19(notR[19], R[19]);
not not1_20(notR[20], R[20]);
not not1_21(notR[21], R[21]);
not not1_22(notR[22], R[22]);
not not1_23(notR[23], R[23]);
not not1_24(notR[24], R[24]);
not not1_25(notR[25], R[25]);
not not1_26(notR[26], R[26]);
not not1_27(notR[27], R[27]);
//and1 gate
and and1_0(ANc1[0], notR[0], ANe[0]);
and and1_1(ANc1[1], notR[1], ANe[1]);
and and1_5(ANc1[5], notR[2], ANe[5]);
and and1_2(ANc1[2], notR[3], ANe[2]);
and and1_22(ANc1[22], notR[4], ANe[22]);
and and1_6(ANc1[6], notR[5], ANe[6]);
and and1_12(ANc1[12], notR[6], ANe[12]);
and and1_3(ANc1[3], notR[7], ANe[3]);
and and1_10(ANc1[10], notR[8], ANe[10]);
and and1_23(ANc1[23], notR[9], ANe[23]);
and and1_25(ANc1[25], notR[10], ANe[25]);
and and1_7(ANc1[7], notR[11], ANe[7]);
and and1_18(ANc1[18], notR[12], ANe[18]);
and and1_13(ANc1[13], notR[13], ANe[13]);
and and1_27(ANc1[27], notR[14], ANe[27]);
and and1_4(ANc1[4], notR[15], ANe[4]);
and and1_21(ANc1[21], notR[16], ANe[21]);
and and1_11(ANc1[11], notR[17], ANe[11]);
and and1_9(ANc1[9], notR[18], ANe[9]);
and and1_24(ANc1[24], notR[19], ANe[24]);
and and1_17(ANc1[17], notR[20], ANe[17]);
and and1_26(ANc1[26], notR[21], ANe[26]);
and and1_20(ANc1[20], notR[22], ANe[20]);
and and1_8(ANc1[8], notR[23], ANe[8]);
and and1_16(ANc1[16], notR[24], ANe[16]);
and and1_19(ANc1[19], notR[25], ANe[19]);
and and1_15(ANc1[15], notR[26], ANe[15]);
and and1_14(ANc1[14], notR[27], ANe[14]);
//or gate
or or_14(ANc2[14], R[0], ANe[14]);
or or_15(ANc2[15], R[1], ANe[15]);
or or_19(ANc2[19], R[2], ANe[19]);
or or_16(ANc2[16], R[3], ANe[16]);
or or_8(ANc2[8], R[4], ANe[8]);
or or_20(ANc2[20], R[5], ANe[20]);
or or_26(ANc2[26], R[6], ANe[26]);
or or_17(ANc2[17], R[7], ANe[17]);
or or_24(ANc2[24], R[8], ANe[24]);
or or_9(ANc2[9], R[9], ANe[9]);
or or_11(ANc2[11], R[10], ANe[11]);
or or_21(ANc2[21], R[11], ANe[21]);
or or_4(ANc2[4], R[12], ANe[4]);
or or_27(ANc2[27], R[13], ANe[27]);
or or_13(ANc2[13], R[14], ANe[13]);
or or_18(ANc2[18], R[15], ANe[18]);
or or_7(ANc2[7], R[16], ANe[7]);
or or_25(ANc2[25], R[17], ANe[25]);
or or_23(ANc2[23], R[18], ANe[23]);
or or_10(ANc2[10], R[19], ANe[10]);
or or_3(ANc2[3], R[20], ANe[3]);
or or_12(ANc2[12], R[21], ANe[12]);
or or_6(ANc2[6], R[22], ANe[6]);
or or_22(ANc2[22], R[23], ANe[22]);
or or_2(ANc2[2], R[24], ANe[2]);
or or_5(ANc2[5], R[25], ANe[5]);
or or_1(ANc2[1], R[26], ANe[1]);
or or_0(ANc2[0], R[27], ANe[0]);
//check
assign check = ANc1 % 29;
assign ANc = (check == 5'd0) ? ANc1 : ANc2;
assign Nc = ANc / 29;
endmodule