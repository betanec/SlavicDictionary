using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Verb;

/// <summary>
/// Тип причастия
/// </summary>
public enum ParticipleType : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Настоящее")]
    Present = 1,

    [Display(Name = "Прошедшее")]
    Past = 2,

    [Display(Name = "Будущее")]
    Future = 3,

    [Display(Name = "Перфектное")]
    Perfect = 4
}
