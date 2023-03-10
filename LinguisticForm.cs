using SlavonicLanguageCorpus.Core.Enums.Thesaurus;
using SlavonicLanguageCorpus.Core.Enums.Thesaurus.Numeral;
using SlavonicLanguageCorpus.Core.Enums.Thesaurus.Pronoun;
using SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;
using SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

namespace SlavonicLanguageCorpus.Core.Entities.Thesaurus;

public class LinguisticForm
{
    /// <summary>
    /// Лемма слова
    /// </summary>
    public string Lemma { get; set; }
    /// <summary>
    /// Словоформа
    /// </summary>
    public string Word { get; set; }
    /// <summary>
    /// Форма настоящего времени
    /// </summary>
    public string PresentTenseForm { get; set; }

    /// <summary>
    /// Часть речи
    /// </summary>
    public PartOfSpeech PartOfSpeech { get; set; }

    #region Общее

    /// <summary>
    /// Падеж
    /// </summary>
    public GrammaticalCase GrammaticalCase { get; set; }

    /// <summary>
    /// Род
    /// </summary>
    public GrammaticalGender GrammaticalGender { get; set; }

    /// <summary>
    /// Степень сравнения
    /// </summary>
    public DegreeOfComparison DegreeOfComparison { get; set; }

    /// <summary>
    /// Число
    /// </summary>
    public GrammaticalNumber GrammaticalNumber { get; set; }

    /// <summary>
    /// Полнота / краткость
    /// </summary>
    public CompletenessConcisenessCategory CompletenessConcisenessCategory { get; set; }

    /// <summary>
    /// Лицо
    /// </summary>
    public GrammaticalPerson GrammaticalPerson { get; set; }

    /// <summary>
    /// Личность/ неличность
    /// </summary>
    public PersonalityCategory PersonalityCategory { get; set; }
    #endregion

    #region Глаголы

    /// <summary>
    /// Репрезентация глагола
    /// </summary>
    public VerbRepresentation VerbRepresentation { get; set; }
    
    /// <summary>
    /// Наклонение глагола
    /// </summary>
    public GrammaticalMood GrammaticalMood { get; set; }

    /// <summary>
    /// Время
    /// </summary>
    public Tense Tense { get; set; }

    /// <summary>
    /// Тип причастия
    /// </summary>
    public ParticipleType ParticipleType { get; set; }

    /// <summary>
    /// Залог причастия
    /// </summary>
    public Voice Voice { get; set; }
    #endregion

    #region Местоимения
    /// <summary>
    /// Разряд местоимения
    /// </summary>
    public PronounType PronounType { get; set; }
    #endregion

    #region Числительное
    /// <summary>
    /// Разряд числительного
    /// </summary>
    public NumeralType NumeralType { get; set; }
    #endregion
}
