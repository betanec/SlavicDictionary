using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

public enum GrammaticalGender : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Мужской")]
    Masculine = 1,

    [Display(Name = "Женский")]
    Feminine = 2,

    [Display(Name = "Средний")]
    Neuter = 3,

    [Display(Name = "Без рода")]
    No = 4,

    [Display(Name = "Общий (м-ж)")]
    Common = 5
}
