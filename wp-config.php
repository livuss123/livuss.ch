<?php

define( 'WP_CACHE', true );

/**
 * Grundeinstellungen für WordPress
 *
 * Diese Datei wird zur Erstellung der wp-config.php verwendet.
 * Du musst aber dafür nicht das Installationsskript verwenden.
 * Stattdessen kannst du auch diese Datei als „wp-config.php“ mit
 * deinen Zugangsdaten für die Datenbank abspeichern.
 *
 * Diese Datei beinhaltet diese Einstellungen:
 *
 * * Datenbank-Zugangsdaten,
 * * Tabellenpräfix,
 * * Sicherheitsschlüssel
 * * und ABSPATH.
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Datenbank-Einstellungen - Diese Zugangsdaten bekommst du von deinem Webhoster. ** //
/**
 * Ersetze datenbankname_hier_einfuegen
 * mit dem Namen der Datenbank, die du verwenden möchtest.
 */
define( 'DB_NAME', "efarinit_wp2" );

/**
 * Ersetze benutzername_hier_einfuegen
 * mit deinem Datenbank-Benutzernamen.
 */
define( 'DB_USER', "root" );

/**
 * Ersetze passwort_hier_einfuegen mit deinem Datenbank-Passwort.
 */
define( 'DB_PASSWORD', "" );

/**
 * Ersetze localhost mit der Datenbank-Serveradresse.
 */
define( 'DB_HOST', "localhost" );

/**
 * Der Datenbankzeichensatz, der beim Erstellen der
 * Datenbanktabellen verwendet werden soll
 */
define( 'DB_CHARSET', 'utf8mb4' );

/**
 * Der Collate-Type sollte nicht geändert werden.
 */
define( 'DB_COLLATE', '' );

/**#@+
 * Sicherheitsschlüssel
 *
 * Ändere jeden untenstehenden Platzhaltertext in eine beliebige,
 * möglichst einmalig genutzte Zeichenkette.
 * Auf der Seite {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * kannst du dir alle Schlüssel generieren lassen.
 *
 * Du kannst die Schlüssel jederzeit wieder ändern, alle angemeldeten
 * Benutzer müssen sich danach erneut anmelden.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'HXdhic2>Rc)N12. 1#QK2--rhtBtB[N&g1xfNJa>MTZ7B}PcxV_!`RAy+sL9FTTH' );
define( 'SECURE_AUTH_KEY',  ' 2Lv-DJJR:?B=T{+*-JJV6 <x%MVP!mqP}SuE+Ef%Bb^Tu9k`?=1AA6V$1k)=/Dm' );
define( 'LOGGED_IN_KEY',    '2_waVe_-/=UUO4|}zeg>f4apnUTY]90oO{vR6!AZ*S|<miH5xcW_F#JZgjmDBEfs' );
define( 'NONCE_KEY',        '-f@%;z${UHxh9lLX}Vt&31,b7{R@+-QP|0hvuqqK[n X $mjk0I8z&12bx/w;@|F' );
define( 'AUTH_SALT',        'V+N~1d]2=O8wd(!%b`eOZ`1Z7|z8JJOxVd6ilI.mKT>-DrxS_1I,HwLqTvmWs+%J' );
define( 'SECURE_AUTH_SALT', 'L$gSYdy+%JJCT24I0U`c81N&zw6D]$2]GF>tM*6[9*H+`sF*x)LPbGG.CZmxdkhM' );
define( 'LOGGED_IN_SALT',   '?D<n^A/yWNVa3 X27a8W*>N.CzOlD({M;Ze=(gM6usZngO%JE-:98-@tlDz;.NE;' );
define( 'NONCE_SALT',       '(zZ:dArS%[1pZc1/oH 7Q}LVq1Z->5v^6|,<eF9+)pUciY GKld.ed=f[P_6*=}d' );

/**#@-*/

/**
 * WordPress Datenbanktabellen-Präfix
 *
 * Wenn du verschiedene Präfixe benutzt, kannst du innerhalb einer Datenbank
 * verschiedene WordPress-Installationen betreiben.
 * Bitte verwende nur Zahlen, Buchstaben und Unterstriche!
 */
$table_prefix = 'wp_';

/**
 * Für Entwickler: Der WordPress-Debug-Modus.
 *
 * Setze den Wert auf „true“, um bei der Entwicklung Warnungen und Fehler-Meldungen angezeigt zu bekommen.
 * Plugin- und Theme-Entwicklern wird nachdrücklich empfohlen, WP_DEBUG
 * in ihrer Entwicklungsumgebung zu verwenden.
 *
 * Besuche den Codex, um mehr Informationen über andere Konstanten zu finden,
 * die zum Debuggen genutzt werden können.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );

/* Füge individuelle Werte zwischen dieser Zeile und der „Schluss mit dem Bearbeiten“ Zeile ein. */



/* Das war’s, Schluss mit dem Bearbeiten! Viel Spaß. */
/* That's all, stop editing! Happy publishing. */

/** Der absolute Pfad zum WordPress-Verzeichnis. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname(__FILE__) . '/' );
}

/** Definiert WordPress-Variablen und fügt Dateien ein.  */
require_once ABSPATH . 'wp-settings.php';

define( 'WP_MEMORY_LIMIT', '40M' );

