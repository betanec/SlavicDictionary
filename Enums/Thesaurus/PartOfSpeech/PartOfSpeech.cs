using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus;

/// <summary>
/// Часть речи
/// </summary>
public enum PartOfSpeech : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Глагол")]
    Verb = 1,

    [Display(Name = "Предикатив")]
    Predicative = 2,

    [Display(Name = "Междометие")]
    Interjection = 3,

    [Display(Name = "Предлог")]
    Preposition = 4,

    [Display(Name = "Местоимение")]
    Pronoun = 5,

    [Display(Name = "Союз")]
    Conjunction = 6,

    [Display(Name = "Прилагательное")]
    Adjective = 7,

    [Display(Name = "Существительное")]
    Noun = 8,

    [Display(Name = "Частица")]
    Particle = 9,

    [Display(Name = "Наречие")]
    Adverb = 10,

    [Display(Name = "Число")]
    Number = 11,

    [Display(Name = "Числительное")]
    Numeral = 12
}
