## Caso de estudio: Editor de formas y undo/redo
Este editor gráfico permite cambiar el color y la posición de las formas en pantalla. Cualquier modificación puede deshacerse y repetirse (undo, redo).

El “undo” (deshacer) se basa en la colaboración entre los patrones Memento y Command. El editor rastrea un historial de comandos ejecutados. Antes de ejecutar cualquier comando, realiza una copia de seguridad y la conecta al objeto de comando. Tras la ejecución, empuja el comando ejecutado al historial.

Cuando un usuario solicita deshacer, el editor extrae un comando reciente del historial y restaura el estado desde la copia de seguridad guardada dentro de ese comando. Si el usuario requiere un nuevo undo, el editor extrae el siguiente comando del historial y así sucesivamente.

Los comandos revertidos se mantienen en el historial hasta que el usuario realice modificaciones en las formas en pantalla. Esto es fundamental para rehacer comandos deshechos.
