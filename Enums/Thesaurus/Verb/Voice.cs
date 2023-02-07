using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

/// <summary>
/// Залог (причастия)
/// </summary>
public enum Voice : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Действительный")]
    Active = 1,

    [Display(Name = "Страдательный")]
    Passive = 2    
}
