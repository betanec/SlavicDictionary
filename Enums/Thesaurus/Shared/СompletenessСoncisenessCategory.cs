using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

/// <summary>
/// Полнота/ краткость
/// </summary>
public enum СompletenessСoncisenessCategory : byte
{
    [Display(Name = "Не указана")]
    NotSet = 0,

    [Display(Name = "Полное")]
    Full = 1,

    [Display(Name = "Краткое")]
    Short  = 2
}
