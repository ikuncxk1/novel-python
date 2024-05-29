# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthorCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    invite_code = models.CharField(unique=True, max_length=100)
    validity_time = models.DateTimeField()
    is_used = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_code'


class AuthorIncome(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_id = models.PositiveBigIntegerField()
    book_id = models.PositiveBigIntegerField()
    income_month = models.DateField()
    pre_tax_income = models.PositiveIntegerField()
    after_tax_income = models.PositiveIntegerField()
    pay_status = models.PositiveIntegerField()
    confirm_status = models.PositiveIntegerField()
    detail = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_income'


class AuthorIncomeDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_id = models.PositiveBigIntegerField()
    book_id = models.PositiveBigIntegerField()
    income_date = models.DateField()
    income_account = models.PositiveIntegerField()
    income_count = models.PositiveIntegerField()
    income_number = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_income_detail'


class AuthorInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(unique=True)
    invite_code = models.CharField(max_length=20)
    pen_name = models.CharField(max_length=20)
    tel_phone = models.CharField(max_length=20, blank=True, null=True)
    chat_account = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    work_direction = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_info'


class BookCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    work_direction = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    sort = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_category'


class BookChapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_id = models.PositiveBigIntegerField()
    chapter_num = models.PositiveSmallIntegerField()
    chapter_name = models.CharField(max_length=100)
    word_count = models.PositiveIntegerField()
    is_vip = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_chapter'
        unique_together = (('book_id', 'chapter_num'),)


class BookComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    comment_content = models.CharField(max_length=512)
    reply_count = models.PositiveIntegerField()
    audit_status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_comment'
        unique_together = (('book_id', 'user_id'),)


class BookCommentCopy1(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    comment_content = models.CharField(max_length=512)
    reply_count = models.PositiveIntegerField()
    audit_status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_comment_copy1'
        unique_together = (('book_id', 'user_id'),)


class BookCommentReply(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    reply_content = models.CharField(max_length=512)
    audit_status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_comment_reply'


class BookContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    chapter_id = models.PositiveBigIntegerField(unique=True)
    content = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_content'


class BookInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    work_direction = models.PositiveIntegerField(blank=True, null=True)
    category_id = models.PositiveBigIntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    pic_url = models.CharField(max_length=200)
    book_name = models.CharField(max_length=50)
    author_id = models.PositiveBigIntegerField()
    author_name = models.CharField(max_length=50)
    book_desc = models.CharField(max_length=2000)
    score = models.PositiveIntegerField()
    book_status = models.PositiveIntegerField()
    visit_count = models.PositiveBigIntegerField()
    word_count = models.PositiveIntegerField()
    comment_count = models.PositiveIntegerField()
    last_chapter_id = models.PositiveBigIntegerField(blank=True, null=True)
    last_chapter_name = models.CharField(max_length=50, blank=True, null=True)
    last_chapter_update_time = models.DateTimeField(blank=True, null=True)
    is_vip = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_info'
        unique_together = (('book_name', 'author_name'),)


class HomeBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    book_id = models.PositiveBigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_book'


class HomeFriendLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    link_name = models.CharField(max_length=50)
    link_url = models.CharField(max_length=100)
    sort = models.PositiveIntegerField()
    is_open = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_friend_link'


class NewsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    sort = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_category'


class NewsContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    news_id = models.PositiveBigIntegerField(unique=True)
    content = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_content'


class NewsInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.PositiveBigIntegerField()
    category_name = models.CharField(max_length=50)
    source_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_info'


class PayAlipay(models.Model):
    id = models.BigAutoField(primary_key=True)
    out_trade_no = models.CharField(max_length=64)
    trade_no = models.CharField(max_length=64)
    buyer_id = models.CharField(max_length=16, blank=True, null=True)
    trade_status = models.CharField(max_length=32, blank=True, null=True)
    total_amount = models.PositiveIntegerField()
    receipt_amount = models.PositiveIntegerField(blank=True, null=True)
    invoice_amount = models.PositiveIntegerField(blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_alipay'


class PayWechat(models.Model):
    id = models.BigAutoField(primary_key=True)
    out_trade_no = models.CharField(max_length=32)
    transaction_id = models.CharField(max_length=32)
    trade_type = models.CharField(max_length=16, blank=True, null=True)
    trade_state = models.CharField(max_length=32, blank=True, null=True)
    trade_state_desc = models.CharField(max_length=255, blank=True, null=True)
    amount = models.PositiveIntegerField()
    payer_total = models.PositiveIntegerField(blank=True, null=True)
    success_time = models.DateTimeField(blank=True, null=True)
    payer_openid = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_wechat'


class SysLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    operation = models.CharField(max_length=50, blank=True, null=True)
    time = models.PositiveIntegerField(blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    params = models.CharField(max_length=5000, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_log'


class SysMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200, blank=True, null=True)
    type = models.PositiveIntegerField()
    icon = models.CharField(max_length=50, blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    role_sign = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.PositiveBigIntegerField()
    menu_id = models.PositiveBigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role_menu'


class SysUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.PositiveIntegerField(blank=True, null=True)
    birth = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    role_id = models.PositiveBigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    test = models.IntegerField(blank=True, null=True)
    test2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class UserBookshelf(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    book_id = models.PositiveBigIntegerField()
    pre_content_id = models.PositiveBigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bookshelf'
        unique_together = (('user_id', 'book_id'),)


class UserComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    book_id = models.PositiveBigIntegerField()
    comment_content = models.CharField(max_length=512)
    reply_count = models.PositiveIntegerField()
    audit_status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_comment'
        unique_together = (('book_id', 'user_id'),)


class UserCommentReply(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    reply_content = models.CharField(max_length=512)
    audit_status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_comment_reply'


class UserConsumeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    amount = models.PositiveIntegerField()
    product_type = models.PositiveIntegerField()
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    produc_name = models.CharField(max_length=50, blank=True, null=True)
    produc_value = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_consume_log'


class UserFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    content = models.CharField(max_length=512)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_feedback'


class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=8)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    user_photo = models.CharField(max_length=100, blank=True, null=True)
    user_sex = models.PositiveIntegerField(blank=True, null=True)
    account_balance = models.PositiveBigIntegerField()
    status = models.PositiveIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserPayLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    pay_channel = models.PositiveIntegerField()
    out_trade_no = models.CharField(max_length=64)
    amount = models.PositiveIntegerField()
    product_type = models.PositiveIntegerField()
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255)
    product_value = models.PositiveIntegerField(blank=True, null=True)
    pay_time = models.DateTimeField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pay_log'


class UserReadHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    book_id = models.PositiveBigIntegerField()
    pre_content_id = models.PositiveBigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_read_history'
        unique_together = (('user_id', 'book_id'),)
