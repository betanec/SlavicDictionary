using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

/// <summary>
/// Число
/// </summary>
public enum GrammaticalNumber : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Единственное")]
    Singular = 1,

    [Display(Name = "Множественное")]
    Plural = 2,

    [Display(Name = "Двойственное")]
    Dual = 3
}
