// File Name: ./files/Uni_HL_20221007_0944/ANdecoder_Uni_HL_13_for_N_11.v
// module= 13
// 可更正AN的bit數= 12
// mod的bit數= 4
// 可更正N的bit數= 8

module ANdecoder(ANe, Nc);
input [11:0] ANe;
output [7:0] Nc;
wire [3:0] mod_tri;
wire [3:0] not_mod_tri;
wire [11:0] error_bit;
wire [11:0] ANc;
assign mod_tri = ANe % 13;

//not gate
not not_0(not_mod_tri[0], mod_tri[0]);
not not_1(not_mod_tri[1], mod_tri[1]);
not not_2(not_mod_tri[2], mod_tri[2]);
not not_3(not_mod_tri[3], mod_tri[3]);
//and gate
and and_1(error_bit[6], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3]);
and and_2(error_bit[7], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3]);
and and_3(error_bit[10], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3]);
and and_4(error_bit[8], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and_5(error_bit[3], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and_6(error_bit[11], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and_7(error_bit[5], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and_8(error_bit[9], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and_9(error_bit[2], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and_10(error_bit[4], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and_11(error_bit[1], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and_12(error_bit[0], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3]);
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
assign Nc = ANc / 13;

endmodule