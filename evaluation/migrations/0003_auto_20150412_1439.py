# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_auto_20150412_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='DefaultGroup',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='GeneralScore',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Phrases',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_ADJP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_ADVP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Adj',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Adj_MOD',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Adv_MOD',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Adverb',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_AmbiWord',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_BA_Sen',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_BEI_Sen',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Collocation',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Cons_Verb',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Idiom',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Locate_Phr',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_NP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_NewWord',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Noun',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Noun_MOD',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_OverLapWord',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_PP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Pivot_Phrase',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Predi_Comp',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Predi_Obj',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Prep',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Prep_Obj',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Pron',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_QP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_SHI_Sen',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Sub_Predi',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_VP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_Verb',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='S_YOU_Sen',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Sentences',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Source_FunctionalWords',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Source_Phrases',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Source_SpecialWords',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Source_SubstanWords',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Source_Words',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_ADJP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_ADVP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Adj',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_AdjTrans',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Adj_MOD',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_AdvTrans',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Adv_MOD',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Adverb',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Article',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Be_Predi',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Bleu',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_CONJ_Phr',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_ModalVerb',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_NP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Noun',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_PP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Predi_Obj',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Prep',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Pron',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_QP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Quantity',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Sub_Predi',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_VP',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_Verb',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_WH_Adv_Phr',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_WH_Noun_Phr',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='T_WH_Prep_Phr',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Target_FunctionalWords',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Target_Phrases',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Target_SubstanWords',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Target_Words',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='Words',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='a',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
    ]
