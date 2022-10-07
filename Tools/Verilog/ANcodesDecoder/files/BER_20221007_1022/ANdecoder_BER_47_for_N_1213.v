// File Name: ./files/BER_20221007_1022/ANdecoder_BER_47_for_N_1213.v
// module= 47
// 可更正AN的bit數= 23
// mod的bit數= 6
// 可更正N的bit數= 17

module ANdecoder(ANe, Nc);
input [22:0] ANe;
output [16:0] Nc;
wire [5:0] mod_tri;
wire [5:0] not_mod_tri;
wire [22:0] error_bit;
wire [45:0] and_out;
wire [22:0] ANc;

assign mod_tri = ANe % 47;

//not gate
not not_0(not_mod_tri[0], mod_tri[0]);
not not_1(not_mod_tri[1], mod_tri[1]);
not not_2(not_mod_tri[2], mod_tri[2]);
not not_3(not_mod_tri[3], mod_tri[3]);
not not_4(not_mod_tri[4], mod_tri[4]);
not not_5(not_mod_tri[5], mod_tri[5]);
//and gate
and and_1(and_out[0], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_2(and_out[1], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_3(and_out[2], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_4(and_out[3], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_5(and_out[4], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_6(and_out[5], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_7(and_out[6], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_8(and_out[7], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_9(and_out[8], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_10(and_out[9], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_11(and_out[10], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_12(and_out[11], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_13(and_out[12], mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_14(and_out[13], not_mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_15(and_out[14], mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], not_mod_tri[5]);
and and_16(and_out[15], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_17(and_out[16], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_18(and_out[17], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_19(and_out[18], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_20(and_out[19], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_21(and_out[20], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_22(and_out[21], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_23(and_out[22], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_24(and_out[23], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_25(and_out[24], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_26(and_out[25], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_27(and_out[26], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_28(and_out[27], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_29(and_out[28], mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_30(and_out[29], not_mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_31(and_out[30], mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], mod_tri[4], not_mod_tri[5]);
and and_32(and_out[31], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_33(and_out[32], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_34(and_out[33], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_35(and_out[34], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_36(and_out[35], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_37(and_out[36], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_38(and_out[37], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_39(and_out[38], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_40(and_out[39], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_41(and_out[40], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_42(and_out[41], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_43(and_out[42], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_44(and_out[43], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_45(and_out[44], mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
and and_46(and_out[45], not_mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4], mod_tri[5]);
//or gate
or or_0(error_bit[0], and_out[0], and_out[45]);
or or_1(error_bit[1], and_out[1], and_out[44]);
or or_2(error_bit[2], and_out[3], and_out[42]);
or or_3(error_bit[3], and_out[7], and_out[38]);
or or_4(error_bit[4], and_out[15], and_out[30]);
or or_5(error_bit[5], and_out[14], and_out[31]);
or or_6(error_bit[6], and_out[16], and_out[29]);
or or_7(error_bit[7], and_out[12], and_out[33]);
or or_8(error_bit[8], and_out[20], and_out[25]);
or or_9(error_bit[9], and_out[4], and_out[41]);
or or_10(error_bit[10], and_out[9], and_out[36]);
or or_11(error_bit[11], and_out[19], and_out[26]);
or or_12(error_bit[12], and_out[6], and_out[39]);
or or_13(error_bit[13], and_out[13], and_out[32]);
or or_14(error_bit[14], and_out[18], and_out[27]);
or or_15(error_bit[15], and_out[8], and_out[37]);
or or_16(error_bit[16], and_out[17], and_out[28]);
or or_17(error_bit[17], and_out[10], and_out[35]);
or or_18(error_bit[18], and_out[21], and_out[24]);
or or_19(error_bit[19], and_out[2], and_out[43]);
or or_20(error_bit[20], and_out[5], and_out[40]);
or or_21(error_bit[21], and_out[11], and_out[34]);
or or_22(error_bit[22], and_out[22], and_out[23]);
//xor gate
xor xor_0(ANc[0],error_bit[0],ANe[0]);
xor xor_1(ANc[1],error_bit[1],ANe[1]);
xor xor_2(ANc[2],error_bit[2],ANe[2]);
xor xor_3(ANc[3],error_bit[3],ANe[3]);
xor xor_4(ANc[4],error_bit[4],ANe[4]);
xor xor_5(ANc[5],error_bit[5],ANe[5]);
xor xor_6(ANc[6],error_bit[6],ANe[6]);
xor xor_7(ANc[7],error_bit[7],ANe[7]);
xor xor_8(ANc[8],error_bit[8],ANe[8]);
xor xor_9(ANc[9],error_bit[9],ANe[9]);
xor xor_10(ANc[10],error_bit[10],ANe[10]);
xor xor_11(ANc[11],error_bit[11],ANe[11]);
xor xor_12(ANc[12],error_bit[12],ANe[12]);
xor xor_13(ANc[13],error_bit[13],ANe[13]);
xor xor_14(ANc[14],error_bit[14],ANe[14]);
xor xor_15(ANc[15],error_bit[15],ANe[15]);
xor xor_16(ANc[16],error_bit[16],ANe[16]);
xor xor_17(ANc[17],error_bit[17],ANe[17]);
xor xor_18(ANc[18],error_bit[18],ANe[18]);
xor xor_19(ANc[19],error_bit[19],ANe[19]);
xor xor_20(ANc[20],error_bit[20],ANe[20]);
xor xor_21(ANc[21],error_bit[21],ANe[21]);
xor xor_22(ANc[22],error_bit[22],ANe[22]);
assign Nc = ANc / 47;

endmodule