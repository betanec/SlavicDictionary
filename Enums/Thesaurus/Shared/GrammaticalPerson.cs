using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

/// <summary>
/// Лицо
/// </summary>
public enum GrammaticalPerson : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Первое")]
    First = 1,

    [Display(Name = "Второе")]
    Second = 2,

    [Display(Name = "Третье")]
    Third = 3
}
