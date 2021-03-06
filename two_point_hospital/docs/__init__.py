# -*- coding: utf-8 -*-

from .staff_skill import lt_staff_skill
from .disease_diagnose_and_treatment import lt_disease_diagnose_and_treatment
from .room_info import lt_room_info
from .general_diagnose_one_time_visit_drug_cabinet_threshold import lt_general_diagnose_one_time_visit_drug_cabinet_threshold

doc_data = dict(
    lt_staff_skill=lt_staff_skill,
    lt_disease_diagnose_and_treatment=lt_disease_diagnose_and_treatment,
    lt_room_info=lt_room_info,
    lt_general_diagnose_one_time_visit_drug_cabinet_threshold=lt_general_diagnose_one_time_visit_drug_cabinet_threshold,
)
