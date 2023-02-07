using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

/// <summary>
/// Наклонение глагола
/// </summary>
public enum GrammaticalMood : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Изъявительное")]
    RealisMood = 1,

    [Display(Name = "Повелительное")]
    ImperativeMood = 2,

    [Display(Name = "Сослагательное")]
    ConditionalMood = 3
}
