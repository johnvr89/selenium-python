# features/piano.feature

Feature: Piano Virtual de Musicca
  Como usuario, quiero interactuar con el piano para asegurarme
  de que las teclas son funcionales.

  Scenario: Tocar una melodía simple en el piano
    Given el usuario está en el piano virtual de Musicca
    When el usuario toca 1 vez/veces la melodía de "Estrellita"
    Then la secuencia de notas se completa sin errores

  Scenario: Tocar una melodía 2 veces en el piano
    Given el usuario está en el piano virtual de Musicca
    When el usuario toca 2 vez/veces la melodía de "Estrellita"
    Then la secuencia de notas se completa sin errores

  Scenario: Tocar varias melodías en el piano
    Given el usuario está en el piano virtual de Musicca
    When el usuario toca una nueva melodía
    When el usuario toca 1 vez/veces la melodía de "Estrellita"
    Then la secuencia de notas se completa sin errores
