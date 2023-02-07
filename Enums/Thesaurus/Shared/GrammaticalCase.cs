using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

/// <summary>
/// Падеж
/// </summary>
public enum GrammaticalCase : byte
{
    [Display(Name = "Не указан")]
    NotSet = 0,

    [Display(Name = "Именительный")]
    Nominative = 1,

    [Display(Name = "Родительный")]
    Genitive = 2,

    [Display(Name = "Винительный")]
    Accusative = 3,

    [Display(Name = "Дательный")]
    Dative = 4,

    [Display(Name = "Творительный")]
    Instrumental = 5,

    [Display(Name = "Звательный")]
    Vocative = 6,

    [Display(Name = "Местный")]
    Locative = 7
}
