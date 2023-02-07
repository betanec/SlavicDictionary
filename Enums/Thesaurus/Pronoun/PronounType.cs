using System.ComponentModel.DataAnnotations;

namespace SlavonicLanguageCorpus.Core.Enums.Thesaurus.Pronoun;

/// <summary>
/// Разряд местоимения
/// </summary>
public enum PronounType : byte
{
    [Display(Name = "Не указано")]
    NotSet = 0,

    [Display(Name = "Субстантивное")]
    Substantive = 1,

    [Display(Name = "Определительное")]
    Definitive = 2
}
