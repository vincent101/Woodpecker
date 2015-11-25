from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from index.models import User
from extractor.models import Extractor
from evaluation.models import Evaluation

mode_choice = (
        ('c2e','ChineseToEnglish'),
        ('e2c','EnglishToChinese'),
        )

class EvaluateForm(forms.Form):
    remark = forms.CharField()
    testFile = forms.FileField()
    extractor = forms.ModelChoiceField(queryset=Extractor.objects.all())
    mode = forms.CharField(max_length=10, widget=forms.Select(choices=mode_choice))

    def __unicode__(self):
        return self.remark

def evaluate(request):
    if request.method == "POST":
        ef = EvaluateForm(request.POST, request.FILES)
        if ef.is_valid():
            #user = auth.get_user(request)
            username = request.session.get('username','anybody')
            user = User.objects.get(username = username)
            remark = ef.cleaned_data['remark']
            testFile = ef.cleaned_data['testFile']
            extractor = ef.cleaned_data['extractor']
            mode = ef.cleaned_data['mode']
            remarks = Evaluation.objects.filter(remark__exact = remark)
            if remarks:
                error = 'remark has been used.'
                return render_to_response('evaluation.html',{'ef':ef,'error':error})
            else:
                evaluations = Evaluation()
                evaluations.user = user
                evaluations.remark = remark
                evaluations.testFile = testFile
                evaluations.extractor = extractor
                evaluations.mode = mode
                if mode =='c2e':
                    evaluations.T_Bleu = 0.5826
                    evaluations.S_AmbiWord = 0.5
                    evaluations.S_NewWord = 'None'
                    evaluations.S_Idiom = 'None'
                    evaluations.S_OverLapWord = 'None' 
                    evaluations.S_Collocation = 1
                    evaluations.S_Noun = 0.6264
                    evaluations.S_Verb = 1
                    evaluations.S_Adj = 1
                    evaluations.S_Prep = 'None' 
                    evaluations.S_Adverb = 'None' 
                    evaluations.S_Pron = 'None' 
                    evaluations.S_NP = 0.4167
                    evaluations.S_VP = 0.6176
                    evaluations.S_PP = 'None' 
                    evaluations.S_QP = 0.7353
                    evaluations.S_ADVP = 'None' 
                    evaluations.S_ADJP = 'None' 
                    evaluations.S_Locate_Phr = 0.6
                    evaluations.S_Sub_Predi = 'None' 
                    evaluations.S_Predi_Obj = 'None' 
                    evaluations.S_Predi_Comp = 'None' 
                    evaluations.S_Prep_Obj = 'None' 
                    evaluations.S_Adv_MOD = 'None' 
                    evaluations.S_Adj_MOD = 'None' 
                    evaluations.S_Noun_MOD = 'None' 
                    evaluations.S_Cons_Verb = 'None' 
                    evaluations.S_Pivot_Phrase = 'None' 
                    evaluations.T_Noun = 0.6932
                    evaluations.T_Verb = 0.1667
                    evaluations.T_Adj = 0.2222
                    evaluations.T_Prep = 0.7317
                    evaluations.T_Adverb = 1
                    evaluations.T_Pron = 1
                    evaluations.T_Quantity = 0.9375
                    evaluations.T_AdjTrans = 0.75
                    evaluations.T_AdvTrans = 'None' 
                    evaluations.T_ModalVerb = 'None' 
                    evaluations.T_Article = 'None' 
                    evaluations.T_NP = 0.4401
                    evaluations.T_VP = 0.3475
                    evaluations.T_PP = 0.4252
                    evaluations.T_QP = 1
                    evaluations.T_ADVP = 0.1538
                    evaluations.T_ADJP = 'None' 
                    evaluations.T_WH_Prep_Phr = 'None' 
                    evaluations.T_WH_Adv_Phr = 'None' 
                    evaluations.T_WH_Noun_Phr = 'None' 
                    evaluations.T_CONJ_Phr = 'None' 
                    evaluations.T_Sub_Predi = 0.5349
                    evaluations.T_Predi_Obj = 0.4828
                    evaluations.T_Adv_MOD = 0.8182
                    evaluations.T_Adj_MOD = 0.4352
                    evaluations.T_Be_Predi = 'None' 
                    evaluations.S_BA_Sen = 'None' 
                    evaluations.S_BEI_Sen = 'None' 
                    evaluations.S_SHI_Sen = 'None' 
                    evaluations.S_YOU_Sen = 'None' 
                    evaluations.GeneralScore = 0.4298
                    evaluations.a = 1
                    evaluations.Words = 0.6611
                    evaluations.Phrases = 0.4126
                    evaluations.Sentences = 'None' 
                    evaluations.Source_Words = 0.7174
                    evaluations.Source_Phrases = 0.4114
                    evaluations.Source_FunctionalWords = 'None' 
                    evaluations.Source_SubstanWords = 0.7073
                    evaluations.Source_SpecialWords = 0.8
                    evaluations.Target_Words = 0.6598
                    evaluations.Target_Phrases = 0.4114
                    evaluations.Target_FunctionalWords = 0.7317
                    evaluations.Target_SubstanWords = 0.6598
                    evaluations.DefaultGroup = 0.4398
                if mode == 'e2c':
                    evaluations.T_Bleu = 0.2286
                    #evaluations.S_AmbiWord 
                    #evaluations.S_NewWord
                    #evaluations.S_Idiom
                    #evaluations.S_OverLapWord
                    evaluations.S_Collocation = 0.3333
                    evaluations.S_Noun = 0.4293
                    evaluations.S_Verb = 0.3333
                    evaluations.S_Adj = 0.3846
                    #evaluations.S_Prep
                    evaluations.S_Adverb = 'None' 
                    evaluations.S_Pron = 'None' 
                    evaluations.S_NP = 0.3153
                    evaluations.S_VP = 0.175
                    evaluations.S_PP = 0.2049
                    evaluations.S_QP = 'None' 
                    evaluations.S_ADVP = 'None' 
                    evaluations.S_ADJP = 'None' 
                    #evaluations.S_Locate_Phr
                    evaluations.S_Sub_Predi = 'None' 
                    evaluations.S_Predi_Obj = 0.0714
                    #evaluations.S_Predi_Comp
                    #evaluations.S_Prep_Obj
                    evaluations.S_Adv_MOD = 'None' 
                    evaluations.S_Adj_MOD = 'None' 
                    #evaluations.S_Noun_MOD
                    #evaluations.S_Cons_Verb
                    #evaluations.S_Pivot_Phrase
                    evaluations.T_Noun = 0.3739
                    evaluations.T_Verb = 0.1818
                    evaluations.T_Adj = 'None' 
                    evaluations.T_Prep = 0.8
                    evaluations.T_Adverb = 0
                    evaluations.T_Pron = 0
                    evaluations.T_Quantity = 0.0833
                    #evaluations.T_AdjTrans
                    #evaluations.T_AdvTrans
                    #evaluations.T_ModalVerb
                    #evaluations.T_Article
                    evaluations.T_NP = 0.217
                    evaluations.T_VP = 0.1076
                    evaluations.T_PP = 0.1412
                    evaluations.T_QP = 0.087
                    evaluations.T_ADVP = 'None' 
                    evaluations.T_ADJP = 'None' 
                    #evaluations.T_WH_Prep_Phr
                    #evaluations.T_WH_Adv_Phr
                    #evaluations.T_WH_Noun_Phr
                    #evaluations.T_CONJ_Phr
                    evaluations.T_Sub_Predi = 0.2438
                    evaluations.T_Predi_Obj = 0.1914
                    evaluations.T_Adv_MOD = 0.0532
                    evaluations.T_Adj_MOD = 0.4762
                    #evaluations.T_Be_Predi
                    #evaluations.S_BA_Sen
                    #evaluations.S_BEI_Sen
                    #evaluations.S_SHI_Sen
                    #evaluations.S_YOU_Sen

                    evaluations.S_DicPrep = "None"
                    evaluations.S_Acro = "None"
                    evaluations.S_MWE = "None"
                    evaluations.S_PhrVerb = "None"
                    evaluations.S_Hyperbaton = "None"
                    evaluations.S_AdjTrans = "None"
                    evaluations.s_AdvTrans = "None"
                    evaluations.S_WH_Prep_Phr = "None"
                    evaluations.S_WH_Adv_Phr = "None"
                    evaluations.S_WH_Noun_Phr = "None"
                    evaluations.S_CONJ_Phr = "None"
                    evaluations.S_Be_Predi = "None"
                    evaluations.T_Measure = 0.0667
                    evaluations.T_Locate_Phr = 0.1714
                    evaluations.T_Predi_Comp = "None"
                    evaluations.T_Prep_Obj = 0.1538
                    evaluations.T_Noun_MOD = 0.3137
                    evaluations.S_NormalPresentTense = "None"
                    evaluations.S_PostFutureTense = "None"
                    evaluations.S_FutureTense = "None"
                    evaluations.S_NormalPostTense = 0.3667
                    evaluations.S_PresentCompleteTense = "None"
                    evaluations.S_PostCompleteTense = "None"
                    evaluations.S_FutureCompleteTense = "None"
                    evaluations.S_PostFutureCompleteTense = "None"
                    evaluations.S_PresentDoingTense = "None"
                    evaluations.S_PostDoingTense = "None"
                    evaluations.S_FutureDoingTense = "None"
                    evaluations.S_PostFutureDoingTense = "None"
                    evaluations.S_PresentCompleteDoingTense = "None"
                    evaluations.S_PostCompleteDoingTense = "None"
                    evaluations.S_FutureCompleteDoingTense = "None"
                    evaluations.S_PostFutureCompleteDoingTense = "None"
                    evaluations.S_NormalPresentTense_NOT = "None"
                    evaluations.S_PostFutureTense_NOT = "None"
                    evaluations.S_FutureTense_NOT = "None"
                    evaluations.S_NormalPostTense_NOT = "None"
                    evaluations.S_PresentCompleteTense_NOT = "None"
                    evaluations.S_PostCompleteTense_NOT = "None"
                    evaluations.S_FutureCompleteTense_NOT = "None"
                    evaluations.S_PostFutureCompleteTense_NOT = "None"
                    evaluations.S_PresentDoingTense_NOT = "None"
                    evaluations.S_PostDoingTense = "None"
                    evaluations.S_FutureDoingTense = "None"
                    evaluations.S_PostFutureDoingTense_NOT = "None"
                    evaluations.S_PresentCompleteDoingTense_NOT = "None"
                    evaluations.S_PostCompleteDoingTense_NOT = "None"
                    evaluations.S_FutureCompleteDoingTense_NOT = "None"
                    evaluations.S_PostFutureCompleteDoingTense_NOT = "None"
                    evaluations.S_WhenClause = "None"
                    evaluations.S_WheneverClause = "None"
                    evaluations.S_WhileClause = "None"
                    evaluations.S_BeforeClause = "None"
                    evaluations.S_AfterClause = "None"
                    evaluations.S_UntilClause = "None"
                    evaluations.S_TillClause = "None"
                    evaluations.S_ByTheTimeClause = "None"
                    evaluations.S_AsSoonAsClause = "None"
                    evaluations.S_Hardly_WhenClause = "None"
                    evaluations.S_NoSooner_ThanClause = "None"
                    evaluations.S_TheMomentClause = "None"
                    evaluations.S_TheMinuteClause = "None"
                    evaluations.S_ImmediatelyClause = "None"
                    evaluations.S_DirectlyClause = "None"
                    evaluations.S_InstantlyClause = "None"
                    evaluations.S_BcauseClause = "None"
                    evaluations.S_SinceClause = "None"
                    evaluations.S_NotThatClause = "None"
                    evaluations.S_IfClause = "None"
                    evaluations.S_UnlessClause = "None"
                    evaluations.S_InCaseClause = "None"
                    evaluations.S_AsLongAsClause = "None"
                    evaluations.S_SoThatClause = "None"
                    evaluations.S_InOrderThatClause = "None"
                    evaluations.S_ForFearThatClause = "None"
                    evaluations.S_So_ThatClause = "None"
                    evaluations.S_Such_ThatClause = "None"
                    evaluations.S_ThanClause = "None"
                    evaluations.S_As_AsClause = "None"
                    evaluations.S_So_AsClause = "None"
                    evaluations.S_As_IfClause = "None"
                    evaluations.S_AsThoughClause = "None"
                    evaluations.S_ThoughClause = "None"
                    evaluations.S_AlthoughClause = "None"
                    evaluations.S_EvenIfClause = "None"
                    evaluations.S_EvenThough = "None"
                    evaluations.S_NoMatterWhatClause = "None"
                    evaluations.S_WhatEverClause = "None"
                    evaluations.S_NoMatterWhoClause = "None"
                    evaluations.S_WhoeverClause = "None"
                    evaluations.S_NoMatterWhichClause = "None"
                    evaluations.S_WhicheverClause = "None"
                    evaluations.S_NoMatterHowClause = "None"
                    evaluations.S_HoweverClause = "None"
                    evaluations.S_NoMatterWhenClause = "None"

                    evaluations.GeneralScore = 0.2125
                    #evaluations.a
                    evaluations.Words = 0.3382
                    evaluations.Phrases = 0.1894
                    evaluations.Sentences = 0.3667
                    evaluations.Source_Words = 0.4115
                    evaluations.Source_Phrases = 0.2365
                    evaluations.Source_FunctionalWords = "None"
                    evaluations.Source_SubstanWords = 0.4125
                    evaluations.Source_SpecialWords = 0.3333
                    evaluations.Target_Words = 0.3341
                    evaluations.Target_Phrases = 0.1884
                    evaluations.Target_FunctionalWords = 0.25
                    evaluations.Target_SubstanWords = 0.3436
                    evaluations.DefaultGroup = 0.2125

                    evaluations.b = 0.4293
                    evaluations.Result_Clauses = "None"
                    evaluations.Manner_Clauses = "None"
                    evaluations.Compare_Clauses = "None"
                    evaluations.Tense_Yes = 0.3667
                    evaluations.Tense_No = "None"
                    evaluations.Tense = 0.3667
                    evaluations.Reason_Clauses = "None"
                    evaluations.Concessive_Clauses = "None"
                    evaluations.Purpose_Clauses = "None"
                    evaluations.Clauses = "None"
                    evaluations.Condition_Clauses = "None"
                    evaluations.Time_Clauses = "None"

                evaluations.save()
                error = 'successful.'
                print username, remark
                return render_to_response('evaluation.html',{'ef':ef,'error':error})
    else:
        ef = EvaluateForm()
    return render_to_response('evaluation.html',{'ef':ef})
