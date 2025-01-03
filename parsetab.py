
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DECIMAL DIV ENTERO EULER FACTORIAL LOG MULT PAREN_DER PAREN_IZQ PI PORCENTAJE RESTA SUMAS : EE : E SUMA TE : E RESTA TE : TT : T MULT FT : T DIV FT : FF : PAREN_IZQ E PAREN_DERF : LOG PAREN_IZQ E PAREN_DERF : PIF : EULERT : T PORCENTAJE FF : F FACTORIALF : NN : DECIMALN : ENTERO'
    
_lr_action_items = {'PAREN_IZQ':([0,5,6,12,13,14,15,16,19,],[5,5,19,5,5,5,5,5,5,]),'LOG':([0,5,12,13,14,15,16,19,],[6,6,6,6,6,6,6,6,]),'PI':([0,5,12,13,14,15,16,19,],[7,7,7,7,7,7,7,7,]),'EULER':([0,5,12,13,14,15,16,19,],[8,8,8,8,8,8,8,8,]),'DECIMAL':([0,5,12,13,14,15,16,19,],[10,10,10,10,10,10,10,10,]),'ENTERO':([0,5,12,13,14,15,16,19,],[11,11,11,11,11,11,11,11,]),'$end':([1,2,3,4,7,8,9,10,11,17,20,21,22,23,24,25,27,],[0,-1,-4,-7,-10,-11,-14,-15,-16,-13,-2,-3,-5,-6,-12,-8,-9,]),'SUMA':([2,3,4,7,8,9,10,11,17,18,20,21,22,23,24,25,26,27,],[12,-4,-7,-10,-11,-14,-15,-16,-13,12,-2,-3,-5,-6,-12,-8,12,-9,]),'RESTA':([2,3,4,7,8,9,10,11,17,18,20,21,22,23,24,25,26,27,],[13,-4,-7,-10,-11,-14,-15,-16,-13,13,-2,-3,-5,-6,-12,-8,13,-9,]),'PAREN_DER':([3,4,7,8,9,10,11,17,18,20,21,22,23,24,25,26,27,],[-4,-7,-10,-11,-14,-15,-16,-13,25,-2,-3,-5,-6,-12,-8,27,-9,]),'MULT':([3,4,7,8,9,10,11,17,20,21,22,23,24,25,27,],[14,-7,-10,-11,-14,-15,-16,-13,14,14,-5,-6,-12,-8,-9,]),'DIV':([3,4,7,8,9,10,11,17,20,21,22,23,24,25,27,],[15,-7,-10,-11,-14,-15,-16,-13,15,15,-5,-6,-12,-8,-9,]),'PORCENTAJE':([3,4,7,8,9,10,11,17,20,21,22,23,24,25,27,],[16,-7,-10,-11,-14,-15,-16,-13,16,16,-5,-6,-12,-8,-9,]),'FACTORIAL':([4,7,8,9,10,11,17,22,23,24,25,27,],[17,-10,-11,-14,-15,-16,-13,17,17,17,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'E':([0,5,19,],[2,18,26,]),'T':([0,5,12,13,19,],[3,3,20,21,3,]),'F':([0,5,12,13,14,15,16,19,],[4,4,4,4,22,23,24,4,]),'N':([0,5,12,13,14,15,16,19,],[9,9,9,9,9,9,9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> E','S',1,'p_S','grammar.py',69),
  ('E -> E SUMA T','E',3,'p_E_plus','grammar.py',73),
  ('E -> E RESTA T','E',3,'p_E_minus','grammar.py',77),
  ('E -> T','E',1,'p_E_term','grammar.py',81),
  ('T -> T MULT F','T',3,'p_T_mul','grammar.py',85),
  ('T -> T DIV F','T',3,'p_T_div','grammar.py',89),
  ('T -> F','T',1,'p_T_factor','grammar.py',95),
  ('F -> PAREN_IZQ E PAREN_DER','F',3,'p_F_group','grammar.py',99),
  ('F -> LOG PAREN_IZQ E PAREN_DER','F',4,'p_F_log','grammar.py',103),
  ('F -> PI','F',1,'p_F_pi','grammar.py',109),
  ('F -> EULER','F',1,'p_F_euler','grammar.py',113),
  ('T -> T PORCENTAJE F','T',3,'p_T_percent','grammar.py',117),
  ('F -> F FACTORIAL','F',2,'p_F_factorial','grammar.py',125),
  ('F -> N','F',1,'p_F_number','grammar.py',131),
  ('N -> DECIMAL','N',1,'p_N_decimal','grammar.py',135),
  ('N -> ENTERO','N',1,'p_N_integer','grammar.py',139),
]
