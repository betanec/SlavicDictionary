using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

/// <summary>
/// Recurrence
/// </summary>
public enum GrammaticalMood : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Возвратный")]
    Returnable = 1
}
