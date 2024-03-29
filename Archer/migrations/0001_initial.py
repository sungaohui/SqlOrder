# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-28 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlowQuery',
            fields=[
                ('checksum', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('fingerprint', models.TextField()),
                ('sample', models.TextField()),
                ('first_seen', models.DateTimeField(blank=True, null=True)),
                ('last_seen', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('reviewed_by', models.CharField(blank=True, max_length=20, null=True)),
                ('reviewed_on', models.DateTimeField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '慢日志统计',
                'verbose_name_plural': '慢日志统计',
                'db_table': 'mysql_slow_query_review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SlowQueryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname_max', models.CharField(max_length=64)),
                ('client_max', models.CharField(max_length=64, null=True)),
                ('user_max', models.CharField(max_length=64)),
                ('db_max', models.CharField(default=None, max_length=64, null=True)),
                ('bytes_max', models.CharField(max_length=64, null=True)),
                ('sample', models.TextField()),
                ('ts_min', models.DateTimeField(db_index=True)),
                ('ts_max', models.DateTimeField()),
                ('ts_cnt', models.FloatField(blank=True, null=True)),
                ('query_time_sum', models.FloatField(blank=True, db_column='Query_time_sum', null=True)),
                ('query_time_min', models.FloatField(blank=True, db_column='Query_time_min', null=True)),
                ('query_time_max', models.FloatField(blank=True, db_column='Query_time_max', null=True)),
                ('query_time_pct_95', models.FloatField(blank=True, db_column='Query_time_pct_95', null=True)),
                ('query_time_stddev', models.FloatField(blank=True, db_column='Query_time_stddev', null=True)),
                ('query_time_median', models.FloatField(blank=True, db_column='Query_time_median', null=True)),
                ('lock_time_sum', models.FloatField(blank=True, db_column='Lock_time_sum', null=True)),
                ('lock_time_min', models.FloatField(blank=True, db_column='Lock_time_min', null=True)),
                ('lock_time_max', models.FloatField(blank=True, db_column='Lock_time_max', null=True)),
                ('lock_time_pct_95', models.FloatField(blank=True, db_column='Lock_time_pct_95', null=True)),
                ('lock_time_stddev', models.FloatField(blank=True, db_column='Lock_time_stddev', null=True)),
                ('lock_time_median', models.FloatField(blank=True, db_column='Lock_time_median', null=True)),
                ('rows_sent_sum', models.FloatField(blank=True, db_column='Rows_sent_sum', null=True)),
                ('rows_sent_min', models.FloatField(blank=True, db_column='Rows_sent_min', null=True)),
                ('rows_sent_max', models.FloatField(blank=True, db_column='Rows_sent_max', null=True)),
                ('rows_sent_pct_95', models.FloatField(blank=True, db_column='Rows_sent_pct_95', null=True)),
                ('rows_sent_stddev', models.FloatField(blank=True, db_column='Rows_sent_stddev', null=True)),
                ('rows_sent_median', models.FloatField(blank=True, db_column='Rows_sent_median', null=True)),
                ('rows_examined_sum', models.FloatField(blank=True, db_column='Rows_examined_sum', null=True)),
                ('rows_examined_min', models.FloatField(blank=True, db_column='Rows_examined_min', null=True)),
                ('rows_examined_max', models.FloatField(blank=True, db_column='Rows_examined_max', null=True)),
                ('rows_examined_pct_95', models.FloatField(blank=True, db_column='Rows_examined_pct_95', null=True)),
                ('rows_examined_stddev', models.FloatField(blank=True, db_column='Rows_examined_stddev', null=True)),
                ('rows_examined_median', models.FloatField(blank=True, db_column='Rows_examined_median', null=True)),
                ('rows_affected_sum', models.FloatField(blank=True, db_column='Rows_affected_sum', null=True)),
                ('rows_affected_min', models.FloatField(blank=True, db_column='Rows_affected_min', null=True)),
                ('rows_affected_max', models.FloatField(blank=True, db_column='Rows_affected_max', null=True)),
                ('rows_affected_pct_95', models.FloatField(blank=True, db_column='Rows_affected_pct_95', null=True)),
                ('rows_affected_stddev', models.FloatField(blank=True, db_column='Rows_affected_stddev', null=True)),
                ('rows_affected_median', models.FloatField(blank=True, db_column='Rows_affected_median', null=True)),
                ('rows_read_sum', models.FloatField(blank=True, db_column='Rows_read_sum', null=True)),
                ('rows_read_min', models.FloatField(blank=True, db_column='Rows_read_min', null=True)),
                ('rows_read_max', models.FloatField(blank=True, db_column='Rows_read_max', null=True)),
                ('rows_read_pct_95', models.FloatField(blank=True, db_column='Rows_read_pct_95', null=True)),
                ('rows_read_stddev', models.FloatField(blank=True, db_column='Rows_read_stddev', null=True)),
                ('rows_read_median', models.FloatField(blank=True, db_column='Rows_read_median', null=True)),
                ('merge_passes_sum', models.FloatField(blank=True, db_column='Merge_passes_sum', null=True)),
                ('merge_passes_min', models.FloatField(blank=True, db_column='Merge_passes_min', null=True)),
                ('merge_passes_max', models.FloatField(blank=True, db_column='Merge_passes_max', null=True)),
                ('merge_passes_pct_95', models.FloatField(blank=True, db_column='Merge_passes_pct_95', null=True)),
                ('merge_passes_stddev', models.FloatField(blank=True, db_column='Merge_passes_stddev', null=True)),
                ('merge_passes_median', models.FloatField(blank=True, db_column='Merge_passes_median', null=True)),
                ('innodb_io_r_ops_min', models.FloatField(blank=True, db_column='InnoDB_IO_r_ops_min', null=True)),
                ('innodb_io_r_ops_max', models.FloatField(blank=True, db_column='InnoDB_IO_r_ops_max', null=True)),
                ('innodb_io_r_ops_pct_95', models.FloatField(blank=True, db_column='InnoDB_IO_r_ops_pct_95', null=True)),
                ('innodb_io_r_ops_stddev', models.FloatField(blank=True, db_column='InnoDB_IO_r_ops_stddev', null=True)),
                ('innodb_io_r_ops_median', models.FloatField(blank=True, db_column='InnoDB_IO_r_ops_median', null=True)),
                ('innodb_io_r_bytes_min', models.FloatField(blank=True, db_column='InnoDB_IO_r_bytes_min', null=True)),
                ('innodb_io_r_bytes_max', models.FloatField(blank=True, db_column='InnoDB_IO_r_bytes_max', null=True)),
                ('innodb_io_r_bytes_pct_95', models.FloatField(blank=True, db_column='InnoDB_IO_r_bytes_pct_95', null=True)),
                ('innodb_io_r_bytes_stddev', models.FloatField(blank=True, db_column='InnoDB_IO_r_bytes_stddev', null=True)),
                ('innodb_io_r_bytes_median', models.FloatField(blank=True, db_column='InnoDB_IO_r_bytes_median', null=True)),
                ('innodb_io_r_wait_min', models.FloatField(blank=True, db_column='InnoDB_IO_r_wait_min', null=True)),
                ('innodb_io_r_wait_max', models.FloatField(blank=True, db_column='InnoDB_IO_r_wait_max', null=True)),
                ('innodb_io_r_wait_pct_95', models.FloatField(blank=True, db_column='InnoDB_IO_r_wait_pct_95', null=True)),
                ('innodb_io_r_wait_stddev', models.FloatField(blank=True, db_column='InnoDB_IO_r_wait_stddev', null=True)),
                ('innodb_io_r_wait_median', models.FloatField(blank=True, db_column='InnoDB_IO_r_wait_median', null=True)),
                ('innodb_rec_lock_wait_min', models.FloatField(blank=True, db_column='InnoDB_rec_lock_wait_min', null=True)),
                ('innodb_rec_lock_wait_max', models.FloatField(blank=True, db_column='InnoDB_rec_lock_wait_max', null=True)),
                ('innodb_rec_lock_wait_pct_95', models.FloatField(blank=True, db_column='InnoDB_rec_lock_wait_pct_95', null=True)),
                ('innodb_rec_lock_wait_stddev', models.FloatField(blank=True, db_column='InnoDB_rec_lock_wait_stddev', null=True)),
                ('innodb_rec_lock_wait_median', models.FloatField(blank=True, db_column='InnoDB_rec_lock_wait_median', null=True)),
                ('innodb_queue_wait_min', models.FloatField(blank=True, db_column='InnoDB_queue_wait_min', null=True)),
                ('innodb_queue_wait_max', models.FloatField(blank=True, db_column='InnoDB_queue_wait_max', null=True)),
                ('innodb_queue_wait_pct_95', models.FloatField(blank=True, db_column='InnoDB_queue_wait_pct_95', null=True)),
                ('innodb_queue_wait_stddev', models.FloatField(blank=True, db_column='InnoDB_queue_wait_stddev', null=True)),
                ('innodb_queue_wait_median', models.FloatField(blank=True, db_column='InnoDB_queue_wait_median', null=True)),
                ('innodb_pages_distinct_min', models.FloatField(blank=True, db_column='InnoDB_pages_distinct_min', null=True)),
                ('innodb_pages_distinct_max', models.FloatField(blank=True, db_column='InnoDB_pages_distinct_max', null=True)),
                ('innodb_pages_distinct_pct_95', models.FloatField(blank=True, db_column='InnoDB_pages_distinct_pct_95', null=True)),
                ('innodb_pages_distinct_stddev', models.FloatField(blank=True, db_column='InnoDB_pages_distinct_stddev', null=True)),
                ('innodb_pages_distinct_median', models.FloatField(blank=True, db_column='InnoDB_pages_distinct_median', null=True)),
                ('qc_hit_cnt', models.FloatField(blank=True, db_column='QC_Hit_cnt', null=True)),
                ('qc_hit_sum', models.FloatField(blank=True, db_column='QC_Hit_sum', null=True)),
                ('full_scan_cnt', models.FloatField(blank=True, db_column='Full_scan_cnt', null=True)),
                ('full_scan_sum', models.FloatField(blank=True, db_column='Full_scan_sum', null=True)),
                ('full_join_cnt', models.FloatField(blank=True, db_column='Full_join_cnt', null=True)),
                ('full_join_sum', models.FloatField(blank=True, db_column='Full_join_sum', null=True)),
                ('tmp_table_cnt', models.FloatField(blank=True, db_column='Tmp_table_cnt', null=True)),
                ('tmp_table_sum', models.FloatField(blank=True, db_column='Tmp_table_sum', null=True)),
                ('tmp_table_on_disk_cnt', models.FloatField(blank=True, db_column='Tmp_table_on_disk_cnt', null=True)),
                ('tmp_table_on_disk_sum', models.FloatField(blank=True, db_column='Tmp_table_on_disk_sum', null=True)),
                ('filesort_cnt', models.FloatField(blank=True, db_column='Filesort_cnt', null=True)),
                ('filesort_sum', models.FloatField(blank=True, db_column='Filesort_sum', null=True)),
                ('filesort_on_disk_cnt', models.FloatField(blank=True, db_column='Filesort_on_disk_cnt', null=True)),
                ('filesort_on_disk_sum', models.FloatField(blank=True, db_column='Filesort_on_disk_sum', null=True)),
            ],
            options={
                'verbose_name': '慢日志明细',
                'verbose_name_plural': '慢日志明细',
                'db_table': 'mysql_slow_query_review_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataMaskingColumns',
            fields=[
                ('column_id', models.AutoField(primary_key=True, serialize=False, verbose_name='字段id')),
                ('rule_type', models.IntegerField(choices=[(1, '手机号'), (2, '证件号码'), (3, '银行卡'), (4, '邮箱'), (5, '金额'), (6, '其他')], verbose_name='规则类型')),
                ('active', models.IntegerField(choices=[(0, '未激活'), (1, '激活')], verbose_name='激活状态')),
                ('db_name', models.CharField(max_length=50, verbose_name='数据库名称')),
                ('table_schema', models.CharField(max_length=64, verbose_name='字段所在库名')),
                ('table_name', models.CharField(max_length=64, verbose_name='字段所在表名')),
                ('column_name', models.CharField(max_length=64, verbose_name='字段名')),
                ('column_comment', models.CharField(blank=True, default='', max_length=1024, verbose_name='字段描述')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('sys_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '脱敏字段配置',
                'verbose_name_plural': '脱敏字段配置',
                'db_table': 'data_masking_columns',
            },
        ),
        migrations.CreateModel(
            name='DataMaskingRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_type', models.IntegerField(choices=[(1, '手机号'), (2, '证件号码'), (3, '银行卡'), (4, '邮箱'), (5, '金额'), (6, '其他')], unique=True, verbose_name='规则类型')),
                ('rule_regex', models.CharField(max_length=255, verbose_name='规则脱敏所用的正则表达式，表达式必须分组，隐藏的组会使用****代替')),
                ('hide_group', models.IntegerField(verbose_name='需要隐藏的组')),
                ('rule_desc', models.CharField(blank=True, default='', max_length=100, verbose_name='规则描述')),
                ('sys_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '脱敏规则配置',
                'verbose_name_plural': '脱敏规则配置',
                'db_table': 'data_masking_rules',
            },
        ),
        migrations.CreateModel(
            name='db_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=50, unique=True, verbose_name='数据库名称')),
                ('db_host', models.CharField(max_length=200, verbose_name='数据库地址')),
                ('db_port', models.IntegerField(default=3306, verbose_name='数据库端口')),
                ('db_user', models.CharField(max_length=100, verbose_name='登录的用户名')),
                ('db_user_password', models.CharField(max_length=300, verbose_name='登录的密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '数据库地址配置',
                'verbose_name_plural': '数据库地址配置',
            },
        ),
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=30, verbose_name='数据库名称')),
                ('sqllog', models.TextField(verbose_name='执行的sql查询')),
                ('effect_row', models.BigIntegerField(verbose_name='返回行数')),
                ('cost_time', models.CharField(default='', max_length=10, verbose_name='执行耗时')),
                ('username', models.CharField(max_length=30, verbose_name='操作人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('sys_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'sql查询日志',
                'verbose_name_plural': 'sql查询日志',
                'db_table': 'query_log',
            },
        ),
        migrations.CreateModel(
            name='QueryPrivileges',
            fields=[
                ('privilege_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30, verbose_name='用户名')),
                ('cluster_name', models.CharField(max_length=50, verbose_name='集群名称')),
                ('db_name', models.CharField(max_length=200, verbose_name='数据库')),
                ('table_name', models.CharField(max_length=200, verbose_name='表')),
                ('valid_date', models.DateField(verbose_name='有效时间')),
                ('limit_num', models.IntegerField(default=100, verbose_name='行数限制')),
                ('priv_type', models.IntegerField(choices=[(1, 'DATABASE'), (2, 'TABLE')], default=0, verbose_name='权限类型')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('sys_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '查询权限记录表',
                'verbose_name_plural': '查询权限记录表',
                'db_table': 'query_privileges',
            },
        ),
        migrations.CreateModel(
            name='QueryPrivilegesApply',
            fields=[
                ('apply_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='申请标题')),
                ('user_name', models.CharField(max_length=30, verbose_name='申请人')),
                ('cluster_name', models.CharField(max_length=50, verbose_name='集群名称')),
                ('db_list', models.TextField(verbose_name='数据库')),
                ('table_list', models.TextField(verbose_name='表')),
                ('valid_date', models.DateField(verbose_name='有效时间')),
                ('limit_num', models.IntegerField(default=100, verbose_name='行数限制')),
                ('priv_type', models.IntegerField(choices=[(1, 'DATABASE'), (2, 'TABLE')], default=0, verbose_name='权限类型')),
                ('status', models.IntegerField(choices=[(0, '待审核'), (1, '审核通过'), (2, '审核不通过'), (3, '审核取消')], verbose_name='审核状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('sys_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '查询权限申请记录表',
                'verbose_name_plural': '查询权限申请记录表',
                'db_table': 'query_privileges_apply',
            },
        ),
        migrations.CreateModel(
            name='workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_name', models.CharField(max_length=50, verbose_name='工单内容')),
                ('engineer', models.CharField(max_length=50, verbose_name='发起人')),
                ('review_man', models.CharField(max_length=50, verbose_name='审核人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('finish_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('status', models.CharField(choices=[('已正常结束', '已正常结束'), ('人工终止流程', '人工终止流程'), ('自动审核中', '自动审核中'), ('等待审核人审核', '等待审核人审核'), ('审核通过', '审核通过'), ('定时执行', '定时执行'), ('执行中', '执行中'), ('自动审核不通过', '自动审核不通过'), ('执行有异常', '执行有异常')], max_length=50)),
                ('is_backup', models.CharField(choices=[('否', '否'), ('是', '是')], max_length=20, verbose_name='是否备份')),
                ('review_content', models.TextField(verbose_name='自动审核内容的JSON格式')),
                ('db_name', models.CharField(max_length=50, verbose_name='数据库名称')),
                ('reviewok_time', models.DateTimeField(blank=True, null=True, verbose_name='人工审核通过的时间')),
                ('sql_content', models.TextField(verbose_name='具体sql内容')),
                ('execute_result', models.TextField(blank=True, verbose_name='执行结果的JSON格式')),
                ('is_manual', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否手工执行')),
                ('audit_remark', models.TextField(blank=True, null=True, verbose_name='审核备注')),
            ],
            options={
                'verbose_name': 'SQL工单管理',
                'verbose_name_plural': 'SQL工单管理',
            },
        ),
        migrations.CreateModel(
            name='WorkflowAudit',
            fields=[
                ('audit_id', models.AutoField(primary_key=True, serialize=False)),
                ('workflow_id', models.BigIntegerField(verbose_name='关联业务id')),
                ('workflow_type', models.IntegerField(choices=[(1, '查询权限申请')], verbose_name='申请类型')),
                ('workflow_title', models.CharField(max_length=50, verbose_name='申请标题')),
                ('workflow_remark', models.CharField(default='', max_length=140, verbose_name='申请备注')),
                ('audit_users', models.CharField(max_length=255, verbose_name='审核人列表')),
                ('current_audit_user', models.CharField(max_length=20, verbose_name='当前审核人')),
                ('next_audit_user', models.CharField(max_length=20, verbose_name='下级审核人')),
                ('current_status', models.IntegerField(choices=[(0, '待审核'), (1, '审核通过'), (2, '审核不通过'), (3, '审核取消')], verbose_name='审核状态')),
                ('create_user', models.CharField(max_length=20, verbose_name='申请人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='申请时间')),
                ('sys_time', models.DateTimeField(auto_now=True, verbose_name='系统时间')),
            ],
            options={
                'verbose_name': '工作流列表',
                'verbose_name_plural': '工作流列表',
                'db_table': 'workflow_audit',
            },
        ),
        migrations.CreateModel(
            name='WorkflowAuditDetail',
            fields=[
                ('audit_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('audit_user', models.CharField(max_length=20, verbose_name='审核人')),
                ('audit_time', models.DateTimeField(verbose_name='审核时间')),
                ('audit_status', models.IntegerField(choices=[(0, '待审核'), (1, '审核通过'), (2, '审核不通过'), (3, '审核取消')], verbose_name='审核状态')),
                ('remark', models.CharField(default='', max_length=140, verbose_name='审核备注')),
                ('sys_time', models.DateTimeField(auto_now=True, verbose_name='系统时间')),
                ('audit_id', models.ForeignKey(db_column='audit_id', db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Archer.WorkflowAudit', verbose_name='审核主表id')),
            ],
            options={
                'verbose_name': '审批明细表',
                'verbose_name_plural': '审批明细表',
                'db_table': 'workflow_audit_detail',
            },
        ),
        migrations.CreateModel(
            name='WorkflowAuditSetting',
            fields=[
                ('audit_setting_id', models.AutoField(primary_key=True, serialize=False)),
                ('workflow_type', models.IntegerField(choices=[(1, '查询权限申请')], unique=True, verbose_name='申请类型,')),
                ('audit_users', models.CharField(max_length=255, verbose_name='审核人，单人审核格式为：user1，多级审核格式为：user1,user2')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('sys_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '工作流配置',
                'verbose_name_plural': '工作流配置',
                'db_table': 'workflow_audit_setting',
            },
        ),
        migrations.AlterUniqueTogether(
            name='workflowaudit',
            unique_together=set([('workflow_id', 'workflow_type')]),
        ),
    ]
