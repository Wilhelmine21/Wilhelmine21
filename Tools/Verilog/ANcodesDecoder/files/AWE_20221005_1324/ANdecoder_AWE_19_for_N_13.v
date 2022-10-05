// File Name: ./files/AWE_20221005_1324/ANdecoder_AWE_19_for_N_13.v
// module= 19
// �i��AN��bit��= 9
// mod��bit��= 5
// �i��N��bit��= 4

module ANdecoder(numX, out);
input [8:0] numX;
output [3:0] out;
wire [4:0] mod_tri;
wire [4:0] not_mod_tri;
wire [8:0] error_bit;
wire [17:0] and_out;
wire add;
wire [8:0] AN;

assign mod_tri = numX % 19;

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
or or_9(add, and_out[17], and_out[16], and_out[14], and_out[10], and_out[2], and_out[5], and_out[11], and_out[4], and_out[9]);

assign AN = (add==0) ? numX-error_bit : numX+error_bit;

assign out = AN / 19;

endmodule