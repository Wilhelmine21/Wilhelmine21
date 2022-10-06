// File Name: ./files/BER_20221006_1611/ANdecoder_BER_19_for_N_11.v
// module= 19
// 可更正AN的bit數= 9
// mod的bit數= 5
// 可更正N的bit數= 4

module ANdecoder(ANe, Nc);
input [8:0] ANe;
output [3:0] Nc;
wire [4:0] mod_tri;
wire [4:0] not_mod_tri;
wire [8:0] error_bit;
wire [17:0] and_out;
wire [8:0] ANc;

assign mod_tri = ANe % 19;

//not gate
not not_0(not_mod_tri[0], mod_tri[0]);
not not_1(not_mod_tri[1], mod_tri[1]);
not not_2(not_mod_tri[2], mod_tri[2]);
not not_3(not_mod_tri[3], mod_tri[3]);
not not_4(not_mod_tri[4], mod_tri[4]);
//and gate
and and_1(and_out[0], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_2(and_out[1], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_3(and_out[2], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_4(and_out[3], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_5(and_out[4], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_6(and_out[5], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_7(and_out[6], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3], not_mod_tri[4]);
and and_8(and_out[7], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_9(and_out[8], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_10(and_out[9], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_11(and_out[10], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_12(and_out[11], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_13(and_out[12], mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_14(and_out[13], not_mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_15(and_out[14], mod_tri[0], mod_tri[1], mod_tri[2], mod_tri[3], not_mod_tri[4]);
and and_16(and_out[15], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_17(and_out[16], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
and and_18(and_out[17], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3], mod_tri[4]);
//or gate
or or_0(error_bit[0], and_out[0], and_out[17]);
or or_1(error_bit[1], and_out[1], and_out[16]);
or or_2(error_bit[2], and_out[3], and_out[14]);
or or_3(error_bit[3], and_out[7], and_out[10]);
or or_4(error_bit[4], and_out[2], and_out[15]);
or or_5(error_bit[5], and_out[5], and_out[12]);
or or_6(error_bit[6], and_out[6], and_out[11]);
or or_7(error_bit[7], and_out[4], and_out[13]);
or or_8(error_bit[8], and_out[8], and_out[9]);
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
assign Nc = ANc / 19;

endmodule