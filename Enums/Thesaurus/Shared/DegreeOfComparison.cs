using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

/// <summary>
/// Степень сравнения
/// </summary>
public enum DegreeOfComparison : byte
{
    [Display(Name = "Не указана")]
    NotSet = 0,

    [Display(Name = "Сравнительная")]
    Comparative = 1,

    [Display(Name = "Положительная")]
    Positive = 2
}
