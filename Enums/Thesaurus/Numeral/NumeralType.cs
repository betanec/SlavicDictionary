using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Numeral;

/// <summary>
/// Разряд числительного
/// </summary>
public enum NumeralType : byte
{
    [Display(Name = "Не указан")]
    NotSet = 0,

    [Display(Name = "Собирательное")]
    Collective = 1,

    [Display(Name = "Количественное")]
    Cardinal = 2,

    [Display(Name = "Порядковое")]
    Ordinal = 3
}
