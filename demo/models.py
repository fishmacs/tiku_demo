from django.db import models


class DLQuestion(models.Model):
    info = models.OneToOneField('DLQuestionInfo', primary_key=True, db_column='gid')
    #gid = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)
    temp_id = models.IntegerField()

    class Meta:
        db_table = 'dl_exam_question'


class DLQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=128)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    cp_id = models.IntegerField(null=True)
    chapter_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    zh_Tid = models.CharField(max_length=16)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    ti_order = models.SmallIntegerField(null=True)
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    yid = models.IntegerField()
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "dl_exam_question_index"


class HXQuestion(models.Model):
    info = models.OneToOneField('HXQuestionInfo', primary_key=True, db_column='gid')
    #gid = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)
    temp_id = models.IntegerField()

    class Meta:
        db_table = 'hx_exam_question'


class HXQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=128)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    cp_id = models.IntegerField(null=True)
    chapter_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    zh_Tid = models.CharField(max_length=16)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    ti_order = models.SmallIntegerField(null=True)
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    yid = models.IntegerField()
    downid = models.CharField(max_length=64, null=True)
    downpath = models.CharField(max_length=200, null=True)
    modify_flag = models.SmallIntegerField(default=0)
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "hx_exam_question_index"


class SWQuestion(models.Model):
    info = models.OneToOneField('SWQuestionInfo', primary_key=True, db_column='gid')
    #CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)
    temp_id = models.IntegerField()

    class Meta:
        db_table = 'sw_exam_question'


class SWQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=128)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    cp_id = models.IntegerField(null=True)
    chapter_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    zh_Tid = models.CharField(max_length=16)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    ti_order = models.SmallIntegerField(null=True)
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    yid = models.IntegerField()
    downid = models.CharField(max_length=64, null=True)
    downpath = models.CharField(max_length=200, null=True)
    modify_flag = models.SmallIntegerField(default=0)
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "sw_exam_question_index"


class SXQuestion(models.Model):
    info = models.OneToOneField('SXQuestionInfo', primary_key=True, db_column='gid')
    #gid = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)

    class Meta:
        db_table = 'sx_exam_question'


class SXQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=128)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    cp_id = models.IntegerField(null=True)
    chapter_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    zh_Tid = models.CharField(max_length=16)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    ti_order = models.SmallIntegerField(null=True)
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    yid = models.IntegerField()
    downid = models.CharField(max_length=64, null=True)
    downpath = models.CharField(max_length=200, null=True)
    modify_flag = models.SmallIntegerField(default=0)
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "sx_exam_question_index"


class WLQuestion(models.Model):
    info = models.OneToOneField('WLQuestionInfo', primary_key=True, db_column='gid')
    #gid = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)
    temp_id = models.IntegerField()

    class Meta:
        db_table = 'wl_exam_question'


class WLQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=128)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    cp_id = models.IntegerField(null=True)
    chapter_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    zh_Tid = models.CharField(max_length=16)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    ti_order = models.SmallIntegerField(null=True)
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    yid = models.IntegerField()
    downid = models.CharField(max_length=64, null=True)
    downpath = models.CharField(max_length=200, null=True)
    modify_flag = models.SmallIntegerField(default=0)
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "wl_exam_question_index"


class YWQuestion(models.Model):
    info = models.OneToOneField('YWQuestionInfo', primary_key=True, db_column='gid')
    #gid = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)
    temp_id = models.IntegerField()

    class Meta:
        db_table = 'yw_exam_question'


class YWQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=128)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    cp_id = models.IntegerField(null=True)
    chapter_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    zh_Tid = models.CharField(max_length=16)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    ti_order = models.SmallIntegerField(null=True)
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    yid = models.IntegerField()
    downid = models.CharField(max_length=64, null=True)
    downpath = models.CharField(max_length=200, null=True)
    modify_flag = models.SmallIntegerField(default=0)
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "yw_exam_question_index"


class YYQuestion(models.Model):
    info = models.OneToOneField('YYQuestionInfo', primary_key=True, db_column='gid')
    #gid = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    objective_answer = models.CharField(max_length=64, null=True)
    answer = models.TextField(max_length=32, null=True)
    image = models.TextField(null=True)
    source = models.CharField(max_length=50)
    question_text = models.TextField(null=True)
    column_content = models.TextField()
    analysis = models.TextField()
    repeat_gid = models.CharField(max_length=128)
    temp_id = models.IntegerField()

    class Meta:
        db_table = 'yy_exam_question'


class YYQuestionInfo(models.Model):
    gid = models.CharField(max_length=50, primary_key=True)
    knowledge = models.CharField(max_length=128, null=True)
    zh_knowledge = models.CharField(max_length=128)
    difficulty = models.SmallIntegerField()
    score = models.SmallIntegerField(null=True)
    objective_flag = models.SmallIntegerField()
    option_count = models.SmallIntegerField(null=True)
    group_count = models.SmallIntegerField(null=True)
    question_type = models.CharField(max_length=50)
    update_date = models.DateTimeField(null=True)
    exam_name = models.CharField(max_length=128, null=True)
    subject_id = models.SmallIntegerField()
    grade_id = models.SmallIntegerField(null=True)
    section_id = models.SmallIntegerField(null=True)
    source = models.TextField(null=True)
    state = models.SmallIntegerField(null=True)
    mod_date = models.DateTimeField(null=True)
    downid = models.CharField(max_length=64, null=True)
    downpath = models.CharField(max_length=200, null=True)
    modify_flag = models.SmallIntegerField(default=0)
    disable_flag = models.SmallIntegerField(default=0)
    match_flag = models.SmallIntegerField(default=0)
    knowledge_text = models.CharField(max_length=128, null=True)
    knowledge_id = models.CharField(max_length=128, null=True)
    combine_flag = models.SmallIntegerField(default=0)
    question_template = models.IntegerField(default=0)

    class Meta:
        db_table = "yy_exam_question_index"
