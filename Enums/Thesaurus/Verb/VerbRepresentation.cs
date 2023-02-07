using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

/// <summary>
/// Репрезентация глагола
/// </summary>
public enum VerbRepresentation : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Супин")]
    Supine = 1,

    [Display(Name = "Инфинитив")]
    Infinitive = 2,

    [Display(Name = "Личная форма")]
    PersonalForm = 3,

    [Display(Name = "Причастие")]
    Participle = 4
}
