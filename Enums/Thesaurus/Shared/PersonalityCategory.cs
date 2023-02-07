using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Shared;

/// <summary>
/// Личность/ неличность
/// </summary>
public enum PersonalityCategory : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Личное")]
    Personal = 1,

    [Display(Name = "Неличное")]
    Impersonal = 2
}
