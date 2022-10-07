// File Name: ./files/Uni_LH_20221007_1057/ANdecoder_Uni_LH_13_for_N_252.v
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
wire [11:0] not_error_bit;
wire [11:0] ANc;
assign mod_tri = ANe % 13;

//not0 gate
not not0_0(not_mod_tri[0], mod_tri[0]);
not not0_1(not_mod_tri[1], mod_tri[1]);
not not0_2(not_mod_tri[2], mod_tri[2]);
not not0_3(not_mod_tri[3], mod_tri[3]);
//and0 gate
and and0_1(error_bit[0], mod_tri[0], not_mod_tri[1], not_mod_tri[2], not_mod_tri[3]);
and and0_2(error_bit[1], not_mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3]);
and and0_3(error_bit[4], mod_tri[0], mod_tri[1], not_mod_tri[2], not_mod_tri[3]);
and and0_4(error_bit[2], not_mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and0_5(error_bit[9], mod_tri[0], not_mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and0_6(error_bit[5], not_mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and0_7(error_bit[11], mod_tri[0], mod_tri[1], mod_tri[2], not_mod_tri[3]);
and and0_8(error_bit[3], not_mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and0_9(error_bit[8], mod_tri[0], not_mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and0_10(error_bit[10], not_mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and0_11(error_bit[7], mod_tri[0], mod_tri[1], not_mod_tri[2], mod_tri[3]);
and and0_12(error_bit[6], not_mod_tri[0], not_mod_tri[1], mod_tri[2], mod_tri[3]);
//not1 gate
not not1_0(not_error_bit[0],error_bit[0]);
not not1_1(not_error_bit[1],error_bit[1]);
not not1_2(not_error_bit[2],error_bit[2]);
not not1_3(not_error_bit[3],error_bit[3]);
not not1_4(not_error_bit[4],error_bit[4]);
not not1_5(not_error_bit[5],error_bit[5]);
not not1_6(not_error_bit[6],error_bit[6]);
not not1_7(not_error_bit[7],error_bit[7]);
not not1_8(not_error_bit[8],error_bit[8]);
not not1_9(not_error_bit[9],error_bit[9]);
not not1_10(not_error_bit[10],error_bit[10]);
not not1_11(not_error_bit[11],error_bit[11]);
//and1 gate
and and1_0(ANc[0],not_error_bit[0], ANe[0]);
and and1_1(ANc[1],not_error_bit[1], ANe[1]);
and and1_2(ANc[2],not_error_bit[2], ANe[2]);
and and1_3(ANc[3],not_error_bit[3], ANe[3]);
and and1_4(ANc[4],not_error_bit[4], ANe[4]);
and and1_5(ANc[5],not_error_bit[5], ANe[5]);
and and1_6(ANc[6],not_error_bit[6], ANe[6]);
and and1_7(ANc[7],not_error_bit[7], ANe[7]);
and and1_8(ANc[8],not_error_bit[8], ANe[8]);
and and1_9(ANc[9],not_error_bit[9], ANe[9]);
and and1_10(ANc[10],not_error_bit[10], ANe[10]);
and and1_11(ANc[11],not_error_bit[11], ANe[11]);

assign Nc = ANc / 13;

endmodule