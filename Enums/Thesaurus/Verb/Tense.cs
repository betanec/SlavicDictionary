using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

/// <summary>
/// Время
/// </summary>
public enum Tense : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Настоящее время")]
    Present = 1,

    [Display(Name = "Прошедшее время")]
    Past = 2,

    [Display(Name = "Будущее время")]
    Future = 3,

    [Display(Name = "Aorist")]
    Aorist = 4,

    [Display(Name = "Имперфект")]
    Imperfect = 5
}
