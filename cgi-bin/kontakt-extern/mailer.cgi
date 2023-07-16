#!/usr/bin/perl
#use CGI::Carp "fatalsToBrowser";

# Setup

$offline = "0"; # 0=AUS und 1=AN für Domain-Check
# Hier angeben, ob man nur von bestimmten Adressen Zugriff bekommt. (siehe domains.txt)

$grafikcode = "0"; # 0=AUS und 1=AN für Grafikcode in allen Formularen.

$TimeZoneOffset = '0'; # Zeitzone
# Diese Zeitzone einfach durch die jeweils eigene ersetzen oder stehen lassen. 
# Zeitzonen von -12 über 0 bis +12

$extaus = "0"; # Damit kann man die "Dateiendung überprüfen" Ausschalten.
# Hiermit können sie die Dateiendungsüberprüfen ab- und anschalten. (1=AUS, 0=AN)

$bytes = "5000"; # In Kilobytes angeben
# Hiermit können sie die Grösse der zu schickenden Datei begrenzen(Es muss in Kilobytes angegeben werden!).

$error = "1"; # Fehlermeldung soll auch bei falschem Dateityp oder zu grosser Datei erscheinen - 1=AN   0=AUS
$flood = "1"; # Floodsperre - 1 = AN   0 = AUS
$floodzeit = "10"; # Floodzeit - Dies gibt an, wie lange jemand keine Nachricht absenden darf - Standard: 60 Sekunden

$empfaenger = ''; # Nur Angeben wenn man in den Formularen kein Empfänger angeben möchte im Format name@domain.de
# Definiert einen Empfänger. Sofern ein Empfänger angegeben ist, so werden die Empfänger im Formular ungültig und es wird nur noch dieser Empfänger genutzt.
# Mehrere Empfänger können durch KOMMA getrennt werden.

$ARabsender = ''; # Genau wie $empfaenger funktioniert diese Option für den Absender der automatischen Bestätigung (Autoresponder)
# Optional, kann gesetzt werden wenn ein anderer Absender gewünscht wird, statt der Empfängeradresse.

$multiple = "1"; # 1=Komma, 2=Leerzeile - Hiermit sind Felder mit mehrfacher Auswahl oder gleichen Feldnamen gemeint, wodurch diese getrennt angezeigt werden sollen.
$felder = "1"; # 1=AN, 0=AUS
# Damit werden, sofern man die Sortierung benutzt, nicht ausgefüllte Felder rausgeschnitten, damit die E-Mail wieder "gut" aussieht und lesbar ist.

$felderLINE = "1"; # 1=AN, 0=AUS
# Gleich wie $felder werden die nicht ausgefüllten Felder rausgeschnitten allerdings mit allen nachfolgenden Leerzeilen.

$felderAUTO = "1"; # 1=AN, 0=AUS
# Hiermit werden bei der automatischen generierung der E-Mail die leeren Felder aus- oder eingeblendet.

$gen = "1"; # 1=AN, 0=AUS - Hiermit können automatisiert versteckte Felder (bzgl. <!-- HIDDEN -->) generiert werden. Der Platzhalter ist z.B. für mehrseitige Formulare <!-- HIDDEN -->

$domains = '';
# Hier können Sie alle Domains eintragen, die als Empfänger akzeptiert werden sollen. 
# z.B.: domain.de, meinedomain.de usw. 
# Beachten: OHNE "http://" und "www." davor und auch kein "/" am Ende!!! 
# bzw. auch keine Pfade, lediglich die Domain. 
# Dazu nur Angeben, wenn die obere Funktion "$empfaenger" LEER ist. 
# Wenn Sie diese Funktion nicht nutzen möchten, einfach LEER lassen.
# Auch einzelne E-Mailadressen sind möglich z.B.: support\@domain.de,info\@domain2.de,usw.

$mailprog = ''; # Sollte die automatische Erkennung von Sendmail fehlschlagen. So kann hier manuell der Pfad eingetragen werden.
# LEER lassen wenn der Sendmailpfad automatisch erkannt werden soll.

$temppfad = "/tmp"; # Temppfad für das Zwischenspeichern von temporären Daten
# Generell ist "/tmp" vorhanden ansonsten den internen Pfad zu einem Verzeichnis mit Schreibrecht(min. Zugriffsrecht 666)
# Bei Windows könnte dies z.B. C:/TEMP, C:/TMP, D:/TEMP oder D:/TMP sein.

$smtp = "0"; # 1=AN/SMTP - 0=AUS/Sendmail, hierbei wird festgelegt ob SMTP oder Sendmail genommen wird, um die E-Mails zu versenden.
$timeout = "300"; # In Sekunden angeben, wielange das Script versuchen soll eine SMTP-Verbindung aufzubauen.

$SMTPusername = ''; # Der Zugangsusername zum Versenden einer E-Mail per SMTP, freie SMTP-Server brauchen dies nicht.
$SMTPpassword = ''; # Das Zugangspasswort zum Versenden einer E-Mail per SMTP, freie SMTP-Server brauchen dies nicht.
$SMTPserver = 'localhost'; # z.B.: smtp.domain.de ggf. beim Provider erkundigen.
$SMTPtyp = 'LOGIN'; # Je nach Konfiguration eines Servers werden die Zugangsdaten auch verschlüsselt übertragen.
# Mögliche Typen sind ANONYMOUS, CRAM_MD5, DIGEST_MD5, EXTERNAL, LOGIN, PLAIN

$POP3abfrage = "0"; # 1=AN - 0=AUS, Manche Server verlangen vor dem Versenden einer E-Mail, die Abfrage vom POP3-Postfach.
$POP3username = ''; # Der Zugangsusername um E-Mails abzurufen.
$POP3passwort = ''; # Das Zugangspasswort um E-Mails abzurufen.
$POP3server = 'pop3.domain.tld'; # z.B.: pop3.domain.de ggf. beim Provider erkundigen.

$returnpathconfig = "0"; # 0=AUS und 1=AN - Return-Path
# An den "Return-Path" gehen grundsätzlich die Fehlermeldungen vom MTA(Mail Transport System). 
# z.B.: bei unzustellbaren E-Mails oder wenn das Postfach voll ist. 
# Sollte es zu Versandproblemen kommen, dann diese Funktion deaktivieren.
# Der "Return-Path" wird dann entsprechend der E-Mailadresse vom Empfänger angepasst, falls die Option aktiviert ist.

$rechnen = "1"; # 0=AUS und 1=AN - Rechenoperationen
# Siehe Punkt 12 der Anleitung


$excel = "1"; # 0=AUS und 1=AN - CSV
# Hiermit kann eine CSV-Datei erzeugt werden, weiteres in der Anleitung.
# Diese Option muss aktiviert sein wenn der CSV- bzw. Excel-Export im Formular genutzt werden soll.
# Die E-Mail wird trotzdem versendet. Datei-Anhänge werden nicht mitgespeichert.

$CSVinternerPfad = './mailer-data'; # Option um die CSV-Datei in ein anderes Verzeichnis abzulegen. Falls kein Eintrag vorhanden, wird automatisch $internerPfad verwendet.
$CSVtrennzeichen = '|'; # Trennzeichen für die CSV-Datei
$CSVkopfdaten = '1'; # Speichert die Kopfdaten in der CSV-Datei - 1=Aktiviert, 0=Deaktiviert
$CSVto = '1'; # Speichert die E-Mailadresse vom Empfänger in der CSV-Datei - 1=Aktiviert, 0=Deaktiviert
$CSVfrom = '1'; # Speichert die E-Mailadresse vom Absender in der CSV-Datei - 1=Aktiviert, 0=Deaktiviert
$CSVcc = '1'; # Speichert die CC-Angabe in der CSV-Datei - 1=Aktiviert, 0=Deaktiviert
$CSVbcc = '1'; # Speichert die BCC-Angabe in der CSV-Datei - 1=Aktiviert, 0=Deaktiviert
$CSVumbruch = "\n"; # Bestimmt den Zeilenumbruch z.B. \n, \r, \r\n oder \n\r
$CSVdatei = 'csv.dat'; # Bestimmt die vordefinierte Datei für die CSV-Datei wenn im Formular keine Angabe definiert ist.
$CSVtime  = '1'; # Bestimmt ob Datum und Zeit in der CSV-Datei gespeichert wird. - 1=Aktiviert, 0=Deaktiviert
$CSVtimestamp = '__tag__.__monat__.__jahr__, __stunde__:__minute__'; # Wenn $CSVtime aktiviert, dann können folgende Platzhalter verwendet werden:
# Tag: __tag__, Monat: __monat__, Jahr: __jahr__, Stunde: __stunde__, Minute: __minute__, Sekunde: __sekunde__ und __time__ für den aktuellen Timestamp in Sekunden

$flock = "1"; # 0=AUS - 1=AN - Verhindert Datenverluste bei einem gleichzeitigen Zugriff.
$gzip = "1"; # GZIP Komprimierung - Um den Inhalt schneller und platzsparender zu Übertragen! - 0=AUS - 1=AN

$checkboxOption = "0"; # 0=AUS und 1=AN - 
# Hierdurch werden Checkboxen ohne Valuewert gefiltert, Browser senden beim Anklicken ohne Valuewert ein "on" als Wert mit.

$internerPfad = '.'; # Interner Pfad zu mailer.cgi ohne Dateiname (Nur Angeben wenn Fehlermeldungen kommen das Dateien nicht vollständig gefunden worden!)

# End


#
# Nutzungsbedingungen (Formmailer): 
#  Lizenz: Formmailer
#   Stand: 3.09.2001
#
# Durch Download der Software erklären Sie sich mit diesen Lizenzabkommen einverstanden. 
# Der Formmailer ist Freeware, jedoch nicht zum GNU/GPL - Abkommen zuzuordnen. 
# Diese Lizenz erlaubt es Ihnen, Formmailer zu benutzen. 
# Als Nutzer des Formmailer können Sie auf eigenes Risiko die Software verändern und/oder auf 
# Ihre Bedürfnisse anpassen. Sie können auch Dritte mit der Anpassung/Veränderung beauftragen. 
# Die Original-Software unverändert darf weitergegeben werden jedoch nicht verkauft oder 
# wiederverkauft werden.
#
# Die angepasste/veränderte Software und Teile dieser dürfen nicht weitergegeben, verkauft 
# oder wiederverkauft werden.
#
# Alle Copyright- und Versions-Hinweise, die im Formmailer oder deren HTML-Seiten verwendet, 
# erstellt und/oder gezeigt werden, dürfen nicht entfernt werden. Die Copyright- und Versions-Hinweise 
# müssen für Benutzer sichtbar und in ungeänderter Form dargestellt werden.
#
# Dieses Lizenzabkommen beruht sich auf der aktuellen internationalen Gesetzeslage.
#
# Bei einem Verstoß gegen diesen Lizenzvertrag kann durch die Firma Coder-World oder deren Beauftragten die 
# erworbene Lizenz jederzeit zurückgezogen und für nichtig erklärt werden sowie die Benutzung untersagt werden. 
# Formmailer und die dazugehörenden Dateien werden ohne Funktionsgarantie für die im Umfeld verwendete Hardware 
# oder Software verkauft.
# 
# Coder-World oder deren Beauftragten sind in keiner Form für Inhalte oder Verfasser verantwortlich, die durch 
# diese Software erstellt wurden.
#
# Das Risiko der Benutzung vom Formmailer obliegt dem Lizenznehmer, jegliche Erstattungen im Rechtsfall sind ausgeschlossen. 
# Eine Lizenz ist zeitlich unbegrenzt nutzbar, in der Lizenz ist grundsätzlich der Zugriff auf alle neuen Versionen 
# für einen unbegrenzten Zeitraum enthalten.
#
# Hinweis: Es existieren keine Reseller-, Wiederverkaufs- oder Schüler-/Studenten - 
# Versionen. Nach den Lizenzbedingungen muß der Website-Besitzer die Lizenz selbst erhalten.
#
# Erstellt von www.Coder-World.de
# E-Mail: support@coder-world.de
# Webseite: http://www.coder-world.de
#
# Bei Veröffentlichung dieses Dokuments ist es eine feine Geste, mir eine Nachricht zukommen zu lassen.
binmode(STDOUT);
binmode(STDIN);
$| = 1;
require "$internerPfad/mailer-data/sprache.txt";
$bytes *= 1024;
$version = "1.73";
$domains =~ s/\s//g;
unless(-d("$temppfad")){
	$temppfad = ".";
}

BEGIN {
	use FindBin;
	use lib ("$FindBin::Bin", "$FindBin::Bin/libs");
	$ENV{'TMPDIR'} = $ENV{'TEMP'} || "";

	eval { $died_in_eval = 1; require Compress::Zlib; };
	if($@){
		$zlib = 0;
	}else{
		$zlib = 1;
		import Compress::Zlib;
	}
	if($POP3abfrage == 1){
		eval { $died_in_eval = 1; require Net::POP3; };
		if ($@) {
			$pop3 = 0;
		}else{
			$pop3 = 1;
			import Net::POP3;
		}
	}
	eval { $died_in_eval = 1; require LWP::Simple; };
	if($@){
		$lwpsimple = 0;
	}else{
		$lwpsimple = 1;
		import LWP::Simple;
	}
	if($smtp == 1){
		eval { $died_in_eval = 1; require Net::SMTP_auth; };
		if ($@) {
			$smtpauth = 0;
		}else{
			$smtpauth = 1;
			import Net::SMTP_auth;
		}
	}
	eval { $died_in_eval = 1; require MIME::Base64; };
	if ($@) {
		$base64 = 0;
	}else{
		$base64 = 1;
		import MIME::Base64;
	}
	eval { $died_in_eval = 1; require Image::Magick; };
	if($@){
		$magick = 0;
	}else{
		if($Image::Magick::VERSION){
			$moduleadmin .= "Image::Magick " . $Image::Magick::VERSION . ", ";
		}else{
			$moduleadmin .= "Image::Magick, ";
		}
		$magick = 1;
		import Image::Magick;
	}
	eval { $died_in_eval = 1; require GD; };
	if($@){
		$gd = 0;
	}else{
		if($GD::VERSION){
			$moduleadmin .= "GD " . $GD::VERSION . ", ";
		}else{
			$moduleadmin .= "GD, ";
		}
		$gd = 1;
		import GD;
	}
	eval { $died_in_eval = 1; require String::Random; };
	if ($@) {
		$stringrandom = 0;
	}else{
		$stringrandom = 1;
		import String::Random;
	}
	if($magick or $gd){
		eval { $died_in_eval = 1; require GD::SecurityImage; };
		if ($@) {
			$gdsecurityimage = 0;
		}else{
			$gdsecurityimage = 1;
			import GD::SecurityImage;
		}
	}
}


$sortwert = 1;
foreach (split(/&/,$ENV{'QUERY_STRING'})){
	($namef,$value) = split(/=/,$_,2);
	$namef =~ tr/+/ /;
	$namef =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	if($INFO{$namef}){
		$INFO{$namef} .= ",$value";
		$Multiple{$namef} = 1;
	}else{
		$INFO{$namef} = $value;
	}
}
$INFO{'session'} =~ s/[^\w]//g;

$laenge = $ENV{'CONTENT_LENGTH'};
if($laenge >= ($bytes+2000)){
	close(STDIN);
	&error("$txt{'0'}");
	exit;
}

$OS = $ENV{HTTP_USER_AGENT};
if($OS=~/vms/i){
	$CRLF = "\n";
}elsif($OS=~/^MacOS$/i){
	$CRLF = "\n\r";
}else{
	$CRLF = "\015\012";
}

if($INFO{'session'} && $INFO{'action'} ne "refresh"){
	open(F,">$temppfad/$INFO{'session'}.dat");
	print F $laenge;
	close(F);

	open(F,">$temppfad/$INFO{'session'}.postdata");
	print F "";
	close(F);

	$NEWread = "0";
	open(TMP,">$temppfad/$INFO{'session'}.postdata");
	$fh = select(TMP); $| = 1; select($fh);
	binmode(TMP);
	$pos = 0;
	$aktuelleDateiZahl = 0;

	$boundary = '--'.$2 if($ENV{'CONTENT_TYPE'} =~ /^(.+)boundary=\"?([^\";,]+)\"?$/);

	$DataArt = 0;   #0 = nix, 1 = File, 2 = FormData
	$myDaten = "";

	$oldmethod = 1;

	$DataArt = 0;   #0 = nix, 1 = File, 2 = FormData
	$myDaten = "";

	while(1){
		$TDaten = undef;
		read(STDIN, $TDaten, 20480);
		last unless($TDaten);
		$NEWread += length $TDaten;
		seek(TMP,$pos,0);
		print TMP $NEWread . "\|$aktuelleDateiZahl\|$filename";

		$myDaten .= $TDaten;
		$TDaten = undef;
		if($myDaten !~ /-d*$/){
			if($myDaten =~ /$boundary/){
				@data = split($boundary,$myDaten);
				$test = ($myDaten =~ /^$boundary/)?1:0;
				$myDaten = undef;
				foreach (@data){
					next if(/^$/);
					if($test == 0){
						if($DataArt == 1){
							s/^$CRLF//gs;
							s/$CRLF$//gs;
							$FORM{$feldname} .= $_;
						}elsif($DataArt == 2){
							push @parts, $_;
						}
						$test = 1;
						next;
					}
					if(!/$CRLF$CRLF/){
						$myDaten = $boundary.$_;
						$DataArt = 0;
						next;
					}
					($header,$content) = split(/$CRLF$CRLF/,$_,2);
					($filename) = ($header =~ /; filename="([^"]*?)"/s);
					while ($filename =~ /^\s|\\|\/|:|<|>|\n|\r/) { 
						$filename =~ s/^.*\\//;
						$filename =~ s/^.*\///;
						$filename =~ s/^\s//;
						$filename =~ s/\n//;
						$filename =~ s/\r//;
						$filename =~ s/<//;
						$filename =~ s/>//;
						$filename =~ s/://;
					}
					if($filename){
						($mimetype) = ($header =~ /Content-Type: (.*)/s);
						($feldname) = ($header =~ / name="([^"]*?)"/s);
						$mimetype =~ s/($CRLF.*)//s;

						$DataArt = 1;
						$FILE{$feldname} = $filename;
						$MIME{$feldname} = $mimetype;
						$aktuelleDateiZahl++;
						$FORM{$feldname} .= $content;
						$sortwert++;
						$SORT{$sortwert} = $feldname;
					}else{
						push @parts,$_;
						$DataArt = 2;
					}
					$content = undef;
				}
				@data = ();
			}elsif($DataArt == 1){
				$FORM{$feldname} .= $myDaten;
				$myDaten = undef;
			}elsif($DataArt == 2){
				push @parts, $myDaten;
				$myDaten = undef;
			}
		}
		#$Daten .= $TDaten;
	}
	close(TMP);
	close(STDIN);
	undef $Daten;
}else{
	$NEWread = 0;
	$pos = 0;
	$aktuelleDateiZahl = 0;

	$boundary = '--'.$2 if($ENV{'CONTENT_TYPE'} =~ /^(.+)boundary=\"?([^\";,]+)\"?$/);

	$DataArt = 0;   #0 = nix, 1 = File, 2 = FormData
	$myDaten = "";

	if($boundary){
		$oldmethod = 1;

		while(1){
			$TDaten = undef;
			read(STDIN, $TDaten, 20480);
			last unless($TDaten);
			$NEWread += length $TDaten;

			$myDaten .= $TDaten;
			$TDaten = undef;
			if($myDaten !~ /-d*$/){
				if($myDaten =~ /$boundary/){
					@data = split($boundary,$myDaten);
					$test = ($myDaten =~ /^$boundary/)?1:0;
					$myDaten = undef;
					foreach (@data){
						next if(/^$/);
						if($test == 0){
							if($DataArt == 1){
								s/^$CRLF//gs;
								s/$CRLF$//gs;
								$FORM{$feldname} .= $_;
							}elsif($DataArt == 2){
								push @parts, $_;
							}
							$test = 1;
							next;
						}
						if(!/$CRLF$CRLF/){
							$myDaten = $boundary.$_;
							$DataArt = 0;
							next;
						}
						($header,$content) = split(/$CRLF$CRLF/,$_,2);
						($filename) = ($header =~ /; filename=\"?([^\";,]+)\"?/s);
						while ($filename =~ /^\s|\\|\/|:|<|>|\n|\r/) { 
							$filename =~ s/^.*\\//;
							$filename =~ s/^.*\///;
							$filename =~ s/^\s//;
							$filename =~ s/\n//;
							$filename =~ s/\r//;
							$filename =~ s/<//;
							$filename =~ s/>//;
							$filename =~ s/://;
						}
						if($filename){
							($mimetype) = ($header =~ /Content-Type: (.*)/s);
							($feldname) = ($header =~ / name=\"?([^\";,]+)\"?/s);
							$mimetype =~ s/($CRLF.*)//s;

							$DataArt = 1;
							$FILE{$feldname} = $filename;
							$MIME{$feldname} = $mimetype;
							$aktuelleDateiZahl++;
							$FORM{$feldname} .= $content;
							$sortwert++;
							$SORT{$sortwert} = $feldname;
						}else{
							push @parts,$_;
							$DataArt = 2;
						}
						$content = undef;
					}
					@data = ();
				}elsif($DataArt == 1){
					$FORM{$feldname} .= $myDaten;
					$myDaten = undef;
				}elsif($DataArt == 2){
					push @parts, $myDaten;
					$myDaten = undef;
				}
			}
			#$Daten .= $TDaten;
		}
#		close(TMP);
		close(STDIN);
	}else{
		read(STDIN, $Daten, $laenge);
		@parts = split(/&/, $Daten);
	}
	undef $Daten;
}

foreach (@parts){
	if($boundary){
		($header,$content) = split(/$CRLF$CRLF/,$_,2);
		($namef) = ($header =~ / name=\"?([^\";,]+)\"?/s);
	}else{
		($namef,$content) = split(/=/, $_,2);
	}
	$namef =~ tr/+/ /;
	$namef =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$content =~ tr/+/ /;
	$content =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$content =~ s/$CRLF/\n/g;
	chomp($content);
	if($FORM{$namef}){
		$FORM{$namef} .= ",$content";
		$Multiple{$namef} = 1;
	}else{
		$FORM{$namef} = $content;
	}
	$sortwert++;
	$SORT{$sortwert} = $namef;
}
$action = $FORM{'action'} || $INFO{'action'};

if($action eq "refresh" && $INFO{'i'}){
	&refresh2();
}elsif($action eq "refresh"){
	&refresh();
}
&$action() if($action =~ /^send$|^version$/);
&index;

sub index {
	&check;
	$FORM{'temp'} = $INFO{'temp'} || "index.html" unless($FORM{'temp'});

	if($FORM{'temp'} =~ /^([\w-]+)(\.)([\w-]+)$/){
		open(F,"<$internerPfad/templates/$FORM{'temp'}");
	}else{
		open(F,"<$internerPfad/templates/index.html");
	}
	flock(F,2) if($flock);
	$a_a = join("",<F>);
	flock(F,8) if($flock);
	close(F);
	&error("Die Datei $internerPfad/templates/$FORM{'temp'} wurde nicht vollst&auml;ndig gefunden.") if(!$a_a && $FORM{'temp'});
	if($felder == 1){
		$a_a =~ s/<_(.+?)>//g;
		$a_a =~ s/<__(.+?)>//g;
	}

	&ausgabe($a_a);
}

sub refresh {
	$INFO{'last'} = time;
	$INFO{'startzeit'} = time unless($INFO{'startzeit'});
#	$total = -s "$temppfad/$INFO{'session'}.postdata";
	open(F,"<$temppfad/$INFO{'session'}.postdata");
	($total,$aktuelleDateiZahl,$dateiname) = split(/\|/,<F>);
	close(F);

	open(STAT,"<$temppfad/$INFO{'session'}.dat");
	$total2 = <STAT>;
	close(STAT);
	$total2 = "0" unless($total2);
	$INFO{'total2'} = "0" unless($INFO{'total2'});

	if($INFO{'total'} ne $INFO{'total2'}){
		$INFO{'total'} = $total;
		$INFO{'total2'} = $total2;
	}

	if($total && $total2){
		$percent = $total * 100 / $total2;
	}else{
		$percent = "0";
	}

	$vzeit = time - $INFO{'startzeit'};
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($vzeit);
	$hour -= 1;
	$hour = "0$hour" if($hour < 10);
	$min = "0$min" if($min < 10);
	$sec = "0$sec" if($sec < 10);
	$verstrichen = $hour . ":" . $min . ":" . $sec;

	$speed = 0;
	if($vzeit > 0){
		$bSpeed = $total / $vzeit;
		$kSpeed = $bSpeed / 1024;
	}else{
		$kSpeed = $speed;
	}
	$speed = sprintf("%d",$kSpeed);

	$bRestzeit = $total2 - $total;
	$restzeit = "0";
	if($bSpeed > 0){
		$restzeit = $bRestzeit / $bSpeed;
	}
	$restzeit = sprintf("%d",$restzeit);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($restzeit);
	$hour -= 1;
	$hour = "0$hour" if($hour < 10);
	$min = "0$min" if($min < 10);
	$sec = "0$sec" if($sec < 10);
	$restzeit = $hour . ":" . $min . ":" . $sec;

	($stop1,$stop2,$stop3) = split(/\,/,$INFO{'stopit'});
	$INFO{'total2'} = "0" unless($INFO{'total2'});
	$stopit = $INFO{'total2'} . "," . $stop1 . "," . $stop2;
	if($stopit eq ",," or $stopit eq "0,0,0"){
		if($INFO{'session'}){
			unlink("$temppfad/$INFO{'session'}.dat");
			unlink("$temppfad/$INFO{'session'}.postdata");
		}

		print "Content-Type: text/html\n\n";
		print <<__HTML__;
		<script>
		parent.window.close();
		</script>
		<style>
		table {font-family: Verdana,Arial; font-size: 11px; color: #666666;}
		body {font-family: Verdana,Arial; font-size: 11px; color: #666666;}
		</style>
		</head>
		<body bgcolor="#eeeeee">
		<table border="0" width="100%">
			<tr><td align="center" bgcolor="#ecf8ff">Fehler in der &Uuml;bertragung</td></tr>
		</table>
		</body>
		</html>
__HTML__
		exit;
	}
	$url = "mailer.cgi?stopit=$stopit&action=refresh&total=$INFO{'total'}&total2=$INFO{'total2'}&session=$INFO{'session'}&startzeit=$INFO{'startzeit'}&last=$INFO{'last'}";
	$url =~ s/\n//;

	open(F,"<$internerPfad/templates/uploadanzeige.html");
	$uploadanzeige = join("",<F>);
	close(F);

	print "Content-Type: text/html\n\n";

if($total eq $total2 or $INFO{'total'} eq $INFO{'total2'}){
	if($INFO{'session'}){
		unlink("$temppfad/$INFO{'session'}.dat");
		unlink("$temppfad/$INFO{'session'}.postdata");
	}
	$split .= qq~
		<script>
		parent.window.close();
		</script>
~;
}else{
	$split .= qq~
		<meta HTTP-EQUIV=Refresh CONTENT="1; URL=$url">
~;
}
	$uploadanzeige =~ s/<!-- SPLIT -->/$split/g;
	$uploadanzeige =~ s/__restzeit__/$restzeit/g;
	$uploadanzeige =~ s/__verstrichen__/$verstrichen/g;
	$uploadanzeige =~ s/__dateinamefull__/$dateiname/g;
	if(length($dateiname) > 50){
		$uploadanzeige =~ s/__dateiname__/__dateiname__.../g;
		$uploadanzeige =~ s/__dateiname__/substr($dateiname,0,50)/eg;
	}else{
		$uploadanzeige =~ s/__dateiname__/$dateiname/g;
	}
	$uploadanzeige =~ s/__dateizahl__/$aktuelleDateiZahl/g;
	$uploadanzeige =~ s/__percent__/$percent/g;
	$uploadanzeige =~ s/__speed__/$speed/g;

	if($total < 1024 or $total2 < 1024){
		$uploadanzeige =~ s/__variante__//g;
	}elsif($total < (1024 * 1024) or $total2 < (1024 * 1024)){
		$total = sprintf("%.0f",$total / 1024);
		$total2 = sprintf("%.0f",$total2 / 1024);
		$uploadanzeige =~ s/__variante__/K/g;
	}elsif($total < (1024 * 1024 * 1024) or $total2 < (1024 * 1024 * 1024)){
		$total = sprintf("%.2f",$total / 1024 / 1024);
		$total2 = sprintf("%.2f",$total2 / 1024 / 1024);
		$uploadanzeige =~ s/__variante__/M/g;
	}elsif($total < (1024 * 1024 * 1024 * 1024) or $total2 < (1024 * 1024 * 1024 * 1024)){
		$total = sprintf("%.2f",$total / 1024 / 1024 / 1024);
		$total2 = sprintf("%.2f",$total2 / 1024 / 1024 / 1024);
		$uploadanzeige =~ s/__variante__/G/g;
	}else{
		$total = sprintf("%.2f",$total / 1024 / 1024 / 1024 / 1024);
		$total2 = sprintf("%.2f",$total2 / 1024 / 1024 / 1024 / 1024);
		$uploadanzeige =~ s/__variante__/T/g;
	}
	$uploadanzeige =~ s/__total__/$total/g;
	$uploadanzeige =~ s/__total2__/$total2/g;
	print $uploadanzeige;
	exit;
}

sub version {
	print "Content-Type: text/html\n\n";
	if($base64){
		print $version . "<br>\nModule: MIME::Base64";
	}else{
		print $version;
	}
	exit;
}

sub error {
	local($e) = @_;
	$FORM{'error'} = $FORM{'missing_fields_redirect'} unless($FORM{'error'});

	if($FORM{'error'} =~ /^(http|https):\/\//){
		$FORM{'error'} =~ s/http:/https:/ig if($ENV{'HTTPS'});
		print "Location: $FORM{'error'}\n\n";
		exit;
	}else{
		if($FORM{'error'} =~ /^([\w\/-]+)(\.)([\w-]+)$/){
			open(F,"<$internerPfad/templates/$FORM{'error'}");
		}else{
			open(F,"<$internerPfad/templates/error.html");
		}
	}
	flock(F,2) if($flock);
	$a_a = join("",<F>);
	flock(F,8) if($flock);
	close(F);
	$a_a =~ s!<_fehler>!$e!g;
	unless($a_a){
		print "Content-Type: text/html\n\n";
		if($FORM{'error'} =~ /^([\w\/-]+)(\.)([\w-]+)$/){
			print "Fehler: Die Datei $internerPfad/templates/$FORM{'error'} wurde nicht vollst&auml;ndig gefunden.";
		}else{
			print "Fehler: Die Datei $internerPfad/templates/error.html wurde nicht vollst&auml;ndig gefunden.";
		}
		print "<br>Fehler: $e" if($e);
		exit;
	}

	&ausgabe($a_a);
}

sub send {
	&check;
	unless($mailprog){
		foreach ("/usr/sbin/sendmail"){
			if(-e $_ && -X _){
				$mailprog = $_;
				last;
			}
		}
	}
	if(!$mailprog && !$smtp){
		$errormeldung .= $txt{'1'} . "\n<br>";
	}

	if(-e("$temppfad/$INFO{'session'}.postdata") && $INFO{'session'} =~ /^\w+$/){
		unlink("$temppfad/$INFO{'session'}.dat");
		unlink("$temppfad/$INFO{'session'}.postdata");
	}


	if($FORM{'vorschau'} =~ /^([\w\/-]+)(\.)([\w-]+)$/ && $FORM{'tempv'}){
		$FORM{'fertig'} = $FORM{'vorschau'};
		$FORM{'nextsite'} = 1;
	}

	open(F,"<$internerPfad/mailer-data/zensur.txt");
	flock(F,2) if($flock);
	@zensur = <F>;
	flock(F,8) if($flock);
	close(F);

	$FORM{'aktiv'} = "1.txt" unless($FORM{'aktiv'});
	if($FORM{'aktiv'} =~ /^([\w\/-]+)(\.)([\w-]+)$/){
		open(F,"<$internerPfad/send/$FORM{'aktiv'}");
	}else{
		open(F,"<$internerPfad/send/1.txt");
	}
	flock(F,2) if($flock);
	$aktiv = join("",<F>);
	flock(F,8) if($flock);
	close(F);
	&error("Die Datei ./send/$FORM{'aktiv'} wurde nicht vollst&auml;ndig gefunden.") if(!$aktiv && $FORM{'aktiv'});

	if($FORM{'auto'} =~ /^([\w\/-]+)(\.)([\w-]+)$/){
		open(F,"<$internerPfad/responder/$FORM{'auto'}");
	}else{
		open(F,"<$internerPfad/responder/1.txt");
	}
	flock(F,2) if($flock);
	$aktiv2 = join("",<F>);
	flock(F,8) if($flock);
	close(F);
	$errormeldung .= "Die Datei ./responder/$FORM{'auto'} wurde nicht vollst&auml;ndig gefunden." if(!$aktiv2 && $FORM{'auto'});

	$FORM{'fertig'} = $INFO{'fertig'} || "fertig.html" unless($FORM{'fertig'});
	if($FORM{'fertig'} =~ /^([\w\/-]+)(\.)([\w-]+)$/){
		open(F,"<$internerPfad/templates/$FORM{'fertig'}");
	}else{
		open(F,"<$internerPfad/templates/fertig.html");
	}
	flock(F,2) if($flock);
	$ende = join("",<F>);
	flock(F,8) if($flock);
	close(F);
	$errormeldung .= "Die Datei $internerPfad/templates/$FORM{'fertig'} wurde nicht vollst&auml;ndig gefunden." if(!$ende && $FORM{'fertig'});

	if($grafikcode == 1 && !$FORM{'tempv'} && !$FORM{'nextsite'}){
		$Times = time();
		open(F,"+<mailer-data/sessiongrafik.txt");
		flock(F,2) if($flock);
		@session = <F>;
		seek(F,0,0);
		truncate(F,0);
		foreach(@session){
			s/[\n\r]//g;
			($SESSIONkey,$SESSIONtime) = split(/\|/);
			if($Times < ($SESSIONtime+3600) && lc($SESSIONkey) ne lc($FORM{'grafikcode'})){
				print F $_ . "\n";
			}else{
				$ySESSIONkey = $SESSIONkey;
			}
		}
		flock(F,8) if($flock);
		close(F);
		$errormeldung .= "Der Grafikcode ist falsch.<br>\n" if(lc($FORM{'grafikcode'}) ne lc($ySESSIONkey) or !$FORM{'grafikcode'});
	}

#	open(F,"<deinedatei.pdf");
#	$FORM{'file-upload-50'} = join("",<F>);
#	close(F);
#	$FILE{'file-upload-50'} = "deinedatei.pdf";
#	$MIME{'file-upload-50'} = "application/pdf";
#	$sortwert++;
#	$SORT{$sortwert} = $FILE{'file-upload-50'};

	$FORM{'sort'} = $FORM{'sort_fields'} unless($FORM{'sort'});
	if($FORM{'sort'} && !$FORM{'browsersort'}){
		if($FORM{'nosort'}){
			@feldnamenOLD = keys %FORM;
		}else{
			@feldnamenOLD = sort { $a cmp $b } keys %FORM;
		}
		foreach (split(/,/,$FORM{'sort'})){
			$doppelt{$_} = 1;
		}

		$FORM{'sort'} =~ s/,$//g;
		foreach (@feldnamenOLD){
			unless($doppelt{$_}){
				$FORM{'sort'} .= "," . $_;
			}
		}
		@feldnamen = split(/,/,$FORM{'sort'});
	}elsif($FORM{'nosort'}){
		@feldnamen = keys %FORM;
	}elsif($FORM{'browsersort'}){
		foreach (sort { $a <=> $b } keys %SORT){
			push(@feldnamen,"$SORT{$_}");
		}
	}else{
		@feldnamen = sort { $a cmp $b } keys %FORM;
	}
	if($rechnen == 1){
		$aktiv =~ s/\[<([^>]*)>\]/rechnen($1)/eg;
		$aktiv2 =~ s/\[<([^>]*)>\]/rechnen($1)/eg;
		$ende =~ s/\[<([^>]*)>\]/rechnen($1)/eg;
	}

	foreach $key (@feldnamen){
		if($exist{$key} == 1 or $key eq "" or $key =~ /^x$|^y$|^excel$|^nosort$|^nofrom$|^browsersort$|^sort_fields$|^recipient$|^session$|^to_email$|^email$|^csvyes$|^csvrespond$|^grafikcode$|^action$|^to$|^from$|^fertig$|^sort$|^subject$|^bcc$|^cc$|^back$|^check$|^required$|^checkz$|^next$|^nextsite$|^error$|^auto$|^aktiv$|^htmlresponder$|^html$|^urlcheck$|^mailcheck$|^space$|^vorschau$|^tempv$|^anzahl$|redirect$|^missing_fields_redirect$|^anzahl\d$/){
			if($key && $key !~ /^excel$|^fertig$|^next$|^tempv$|^cc$|^bcc$|^to$|^from$|^nextsite$|^vorschau$|^subject$|^missing_fields_redirect$|^error$/){
				$Bkey = $key;
				$Bkey =~ s/^([readwulsp]+)_//g;

				if($FORM{'html'}){
					$FORM{$key} =~ s/\n/\n<br>/g;
				}elsif($FORM{'htmlresponder'}){
					$FORM{$key} =~ s/\n/\n<br>/g;
				}

				$FORM{'subject'} =~ s/<_$key>/$FORM{$key}/g;
				$FORM{'subject'} =~ s/<__$key>/$key\: $FORM{$key}/g;
				$FORM{'subject'} =~ s/<_$key>/$FORM{$key}/g;
				$FORM{'subject'} =~ s/<__$key>/$key\: $FORM{$key}/g;

				$aktiv =~ s/<_$Bkey>/$FORM{$key}/g;
				$aktiv =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
				$aktiv2 =~ s/<_$Bkey>/$FORM{$key}/g;
				$aktiv2 =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
				$aktiv =~ s/<_$key>/$FORM{$key}/g;
				$aktiv =~ s/<__$key>/$key\: $FORM{$key}/g;
				$aktiv2 =~ s/<_$key>/$FORM{$key}/g;
				$aktiv2 =~ s/<__$key>/$key\: $FORM{$key}/g;

				$FORM{$key} = &txt2html($FORM{$key});
				$generate .= qq~<input type="hidden" name="$key" value="$FORM{$key}">~ if($gen);

				$FORM{$key} =~ s/\n/<br>/g if(!$FORM{'html'} && !$FORM{'htmlresponder'});
				$ende =~ s/<_$Bkey>/$FORM{$key}/g;
				$ende =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
				$ende =~ s/<_$key>/$FORM{$key}/g;
				$ende =~ s/<__$key>/$key\: $FORM{$key}/g;
			}
			next;
		}
		$exist{$key} = 1;

		foreach $ee (@zensur){
			$ee =~ s/[\n\r]//g;
			if($FORM{$key} =~ /$ee/i){
				$newerror = $txt{'2'};
				$newerror =~ s/__ee__/$ee/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}

		if($key =~ /^([readwulsp]+)_/){
			$schalter = $1;
			if($schalter =~ /s/){
				if($FORM{'checks'}){
					$FORM{'checks'} .= ",$key";
				}else{
					$FORM{'checks'} .= "$key";
				}
			}elsif($schalter =~ /r/){
				if($FORM{'check'}){
					$FORM{'check'} .= ",$key";
				}else{
					$FORM{'check'} .= "$key";
				}
			}elsif($schalter =~ /e/){
				if($FORM{'mailcheck'}){
					$FORM{'mailcheck'} .= ",$key";
				}else{
					$FORM{'mailcheck'} .= "$key";
				}
			}elsif($schalter =~ /u/){
				if($FORM{'urlcheck'}){
					$FORM{'urlcheck'} .= ",$key";
				}else{
					$FORM{'urlcheck'} .= "$key";
				}
			}elsif($schalter =~ /d/){
				if($FORM{'checkz'}){
					$FORM{'checkz'} .= ",$key";
				}else{
					$FORM{'checkz'} .= "$key";
				}
			}elsif($schalter =~ /w/){
				if($FORM{'checkaz'}){
					$FORM{'checkaz'} .= ",$key";
				}else{
					$FORM{'checkaz'} .= "$key";
				}
			}elsif($schalter =~ /a/){
				if($FORM{'checka'}){
					$FORM{'checka'} .= ",$key";
				}else{
					$FORM{'checka'} .= "$key";
				}
			}elsif($schalter =~ /l/){
				if($FORM{'checkl'}){
					$FORM{'checkl'} .= ",$key";
				}else{
					$FORM{'checkl'} .= "$key";
				}
			}elsif($schalter =~ /p/){
				if($FORM{'space'}){
					$FORM{'space'} .= ",$key";
				}else{
					$FORM{'space'} .= "$key";
				}
			}
		}
		next if($FORM{$key} eq "" && $felderAUTO);

		if($key =~ /^file-upload-(\d+)$/ && $FILE{$key} ne ""){
			($ext2) = ($FILE{$key} =~ m/\.([^\.]+?)$/);

			if($extaus == 1){
				$wertext = 1;
			}else{
				$wertext = 0;
				open(F,"<$internerPfad/mailer-data/ext.txt");
				flock(F,2) if($flock);
				while(<F>){
					$_ =~ s/[\n\r]//g;
					if(lc($_) eq lc($ext2)){
						$wertext = 1;
						last;
					}
				}
				flock(F,8) if($flock);
				close(F);
			}

			if($wertext == 1 && length($FORM{$key}) < $bytes){
				push(@filenames,"$key");
				$anhang = 1;

				$FORM{'subject'} =~ s/<_$key>/$FORM{$key}/g;
				$FORM{'subject'} =~ s/<__$key>/$key\: $FORM{$key}/g;
				$aktiv =~ s/<_$key>/$FILE{$key}/g;
				$aktiv =~ s/<__$key>/$key\: $FILE{$key}/g;
				$aktiv2 =~ s/<_$key>/$FILE{$key}/g;
				$aktiv2 =~ s/<__$key>/$key\: $FILE{$key}/g;
				$ende =~ s/<_$key>/$FILE{$key}/g;
				$ende =~ s/<__$key>/$key\: $FILE{$key}/g;
				if($FORM{'nokey'} == 1){
					$ausgabe .= "$FILE{$key}\n\n";
				}else{
					$Bkey = $key;
					$Bkey =~ s/^([readwulsp]+)_//g;
					$ausgabe .= "$Bkey\: $FILE{$key}\n\n";
				}
			}else{
				if(length($FORM{$key}) > $bytes){
					$errormeldung .= $txt{'3'} . "\n<br>";
					&error("$txt{'3'}");
				}elsif($wertext ne 1){
					$newerror = $txt{'4'};
					$newerror =~ s/__ext__/$ext2/g;
					$errormeldung .= $newerror . "\n<br>";
				}

				if($FORM{'html'}){
					$FORM{$key} =~ s!&!&amp;!g;
					$FORM{$key} =~ s!&lt;!&#60;!g;
					$FORM{$key} =~ s!&gt;!&#62;!g;
					$FORM{$key} =~ s!<!&lt;!g;
					$FORM{$key} =~ s!>!&gt;!g;
					$FORM{$key} =~ s!\"!&quot;!g;
					chomp($FORM{$key});
					$FORM{$key} =~ s!\n!<br>!g;
				}else{
					chomp($FORM{$key});
				}
				$Bkey = $key;
				$Bkey =~ s/^([readwulsp]+)_//g;

				$FORM{'subject'} =~ s/<_$Bkey>/$FORM{$key}/g;
				$FORM{'subject'} =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
				$FORM{'subject'} =~ s/<_$key>/$FORM{$key}/g;
				$FORM{'subject'} =~ s/<__$key>/$key\: $FORM{$key}/g;
				$aktiv =~ s/<_$Bkey>/$FORM{$key}/g;
				$aktiv =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
				$aktiv2 =~ s/<_$Bkey>/$FORM{$key}/g;
				$aktiv2 =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
				$aktiv =~ s/<_$key>/$FORM{$key}/g;
				$aktiv =~ s/<__$key>/$key\: $FORM{$key}/g;
				$aktiv2 =~ s/<_$key>/$FORM{$key}/g;
				$aktiv2 =~ s/<__$key>/$key\: $FORM{$key}/g;

				if($FORM{'nokey'} == 1){
					$ausgabe .= "$FILE{$key}\n\n";
				}else{
					$ausgabe .= "$Bkey\: $FILE{$key}\n\n";
				}

				if($excel){
					$BKey2 = $key;
					$BKey2 =~ s/[\n\r]/ /g;
					$BKey2 =~ s/$CSVtrennzeichen//g;
					$kopfcsv .= qq~$BKey2$CSVtrennzeichen~;
					$BFormKey = $FORM{$key};
					$BFormKey =~ s/[\n\r]/ /g;
					$BFormKey =~ s/$CSVtrennzeichen//g;
					$csv .= qq~$BFormKey$CSVtrennzeichen~;
				}
				$FORM{$key} = &txt2html($FORM{$key});
				$generate .= qq~<input type="hidden" name="$key" value="$FORM{$key}">~ if($gen);

				$FORM{$key} =~ s/\n/<br>/g if(!$FORM{'html'} && !$FORM{'htmlresponder'});
				$ende =~ s/<_$key>/$FORM{$key}/g;
				$ende =~ s/<__$key>/$key\: $FORM{$key}/g;
				$ende =~ s/<_$Bkey>/$FORM{$key}/g;
				$ende =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
			}
		}else{
			if($FORM{'html'}){
				$FORM{$key} =~ s!&!&amp;!g;
				$FORM{$key} =~ s!&lt;!&#60;!g;
				$FORM{$key} =~ s!&gt;!&#62;!g;
				$FORM{$key} =~ s!<!&lt;!g;
				$FORM{$key} =~ s!>!&gt;!g;
				$FORM{$key} =~ s!\"!&quot;!g;
				chomp($FORM{$key});
				$FORM{$key} =~ s!\n!<br>!g;
			}else{
				chomp($FORM{$key});
			}

			$Bkey = $key;
			$Bkey =~ s/^([readwulsp]+)_//g;
			if($Multiple{$name} == 1 && $multiple == 2){
				if($FORM{'html'}){
					$FORM{$key} =~ s/\,/<br>/g;
				}else{
					$FORM{$key} =~ s/\,/\n/g;
				}
			}
			if($FORM{'nokey'} == 1){
				$ausgabe .= "$FORM{$key}\n\n" if($FORM{$key} !~ /^[Oo][Nn]$/ && $checkboxOption == 1 or !$checkboxOption);
			}else{
				$ausgabe .= "$Bkey\: $FORM{$key}\n\n" if($FORM{$key} !~ /^[Oo][Nn]$/ && $checkboxOption == 1 or !$checkboxOption);
			}

			$FORM{'subject'} =~ s/<_$Bkey>/$FORM{$key}/g;
			$FORM{'subject'} =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
			$FORM{'subject'} =~ s/<_$key>/$FORM{$key}/g;
			$FORM{'subject'} =~ s/<__$key>/$key\: $FORM{$key}/g;
			$aktiv =~ s/<_$Bkey>/$FORM{$key}/g;
			$aktiv =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
			$aktiv2 =~ s/<_$Bkey>/$FORM{$key}/g;
			$aktiv2 =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
			$aktiv =~ s/<_$key>/$FORM{$key}/g;
			$aktiv =~ s/<__$key>/$key\: $FORM{$key}/g;
			$aktiv2 =~ s/<_$key>/$FORM{$key}/g;
			$aktiv2 =~ s/<__$key>/$key\: $FORM{$key}/g;

			if($excel){
				$BKey2 = $key;
				$BKey2 =~ s/[\r\n]/ /g;
				$BKey2 =~ s/$CSVtrennzeichen//g;
				$kopfcsv .= qq~$BKey2$CSVtrennzeichen~;
				$BFormKey = $FORM{$key};
				$BFormKey =~ s/[\r\n]/ /g;
				$BFormKey =~ s/$CSVtrennzeichen//g;
				$csv .= qq~$BFormKey$CSVtrennzeichen~;
			}
			$FORM{$key} = &txt2html($FORM{$key});
			$generate .= qq~<input type="hidden" name="$key" value="$FORM{$key}">~ if($FORM{$key} !~ /^[Oo][Nn]$/ && $gen && $checkboxOption == 1 or $gen && !$checkboxOption);

			$FORM{$key} =~ s/\n/<br>/g if(!$FORM{'html'} && !$FORM{'htmlresponder'});
			$ende =~ s/<_$key>/$FORM{$key}/g;
			$ende =~ s/<__$key>/$key\: $FORM{$key}/g;
			$ende =~ s/<_$Bkey>/$FORM{$key}/g;
			$ende =~ s/<__$Bkey>/$key\: $FORM{$key}/g;
		}
	}
	$ende =~ s/<!--\s*HIDDEN\s*-->/$generate/g if($gen);

	$FORM{'check'} = $FORM{'required'} if($FORM{'required'});
	if($FORM{'check'}){
		foreach (split /\,/,$FORM{'check'}){
			if(!$FORM{$_} or $FORM{$_} =~ /^\s+$/s){
				$_ =~ s/^([readwulsp]+)_//g;
				$newerror = $txt{'5'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($FORM{'checkz'}){
		foreach (split /\,/,$FORM{'checkz'}){
			if($FORM{$_} !~ /^[0-9]+$/){
				$_ =~ s/^([readwulsp]+)_//g;
				$newerror = $txt{'6'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($FORM{'checka'}){
		foreach (split /\,/,$FORM{'checka'}){
			if($FORM{$_} !~ /^[A-Za-z]+$/){
				$_ =~ s/^([readwulsp]+)_//g;
				$newerror = $txt{'7'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($FORM{'checkaz'}){
		foreach (split /\,/,$FORM{'checkaz'}){
			if($FORM{$_} !~ /^[A-Za-z0-9]+$/){
				$_ =~ s/^([readwulsp]+)_//g;
				$newerror = $txt{'8'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($FORM{'checkl'}){
		foreach (split /\,/,$FORM{'checkl'}){
			if($FORM{$_} !~ /^[\sA-Za-z0-9]+$/){
				$_ =~ s/^([readwulsp]+)_//g;
				$newerror = $txt{'9'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($FORM{'checks'}){
		foreach (split /\,/,$FORM{'checks'}){
			if($FORM{$_} !~ /^\s*|\s*$/){
				$FORM{$_} =~ s/^\s*//g;
				$FORM{$_} =~ s/\s*$//g;
			}
		}
	}

	if($FORM{'to'} =~ /^[\w,-]+$/){
		$mailit = $FORM{'to'};
		$FORM{'to'} = "";

		open(F,"<$internerPfad/mailer-data/mail.txt");
		flock(F,2) if($flock);
		while(<F>){
			$_ =~ s/[\n\r]//g;
			($wert,$mail) = split(/=/,$_,2);
			foreach (split(/,/,$mailit)){
				if($wert eq $_){
					$FORM{'to'} .= $mail . ",";
				}
			}
		}
		flock(F,8) if($flock);
		close(F);
		$FORM{'to'} =~ s/,,//g;
		$FORM{'to'} =~ s/,$//g;
	}

	if($FORM{'cc'} =~ /^[\w,-]+$/){
		$mailit = $FORM{'cc'};
		$FORM{'cc'} = "";

		open(F,"<$internerPfad/mailer-data/mail.txt");
		flock(F,2) if($flock);
		while(<F>){
			$_ =~ s/[\n\r]//g;
			($wert,$mail) = split(/=/,$_,2);
			foreach (split(/,/,$mailit)){
				if($wert eq $_){
					$FORM{'cc'} .= $mail . ",";
				}
			}
		}
		flock(F,8) if($flock);
		close(F);
		$FORM{'cc'} =~ s/,,//g;
		$FORM{'cc'} =~ s/,$//g;
	}

	if($FORM{'bcc'} =~ /^[\w,-]+$/){
		$mailit = $FORM{'bcc'};
		$FORM{'bcc'} = "";

		open(F,"<$internerPfad/mailer-data/mail.txt");
		flock(F,2) if($flock);
		while(<F>){
			$_ =~ s/[\n\r]//g;
			($wert,$mail) = split(/=/,$_,2);
			foreach (split(/,/,$mailit)){
				if($wert eq $_){
					$FORM{'bcc'} .= $mail . ",";
				}
			}
		}
		flock(F,8) if($flock);
		close(F);
		$FORM{'bcc'} =~ s/,,//g;
		$FORM{'bcc'} =~ s/,$//g;
	}

	$FORM{'to'} = $FORM{'recipient'} || $FORM{'to_email'} || $empfaenger unless($FORM{'to'});
	if($domains && !$empfaenger){
		foreach (split(/\,/,$FORM{'to'})){
			$mailbackup = $_;
			$back = (split(/\@/,$_))[1];
			$keinerror = "";

			foreach (split(/\,/,$domains)){
				if($_ eq $back or $_ eq $mailbackup){
					$keinerror = 1;
				}
			}

			unless($keinerror){
				$errormeldung .= $txt{'10'} . "\n<br>";
				last;
			}
		}
		if($FORM{'cc'}){
			foreach (split(/\,/,$FORM{'cc'})){
				$mailbackup = $_;
				$back = (split(/\@/,$_))[1];
				$keinerror = "";

				foreach (split(/\,/,$domains)){
					if($_ eq $back or $_ eq $mailbackup){
						$keinerror = 1;
					}
				}

				unless($keinerror){
					$errormeldung .= $txt{'11'} . "\n<br>";
					last;
				}
			}
		}
		if($FORM{'bcc'}){
			foreach (split(/\,/,$FORM{'bcc'})){
				$mailbackup = $_;
				$back = (split(/\@/,$_))[1];
				$keinerror = "";

				foreach (split(/\,/,$domains)){
					if($_ eq $back or $_ eq $mailbackup){
						$keinerror = 1;
					}
				}

				unless($keinerror){
					$errormeldung .= $txt{'12'} . "\n<br>";
					last;
				}
			}
		}
	}

	if(!$FORM{'subject'} && !$FORM{'nextsite'}){
		$errormeldung .= $txt{'13'} . "\n<br>";
	}

	open(F,"<$internerPfad/mailer-data/sperre.txt");
	flock(F,2) if($flock);
	@sperre = <F>;
	flock(F,8) if($flock);
	close(F);

	if($FORM{'mailcheck'}){
		foreach (split(/\,/,$FORM{'mailcheck'})){
			if($FORM{$_} !~ /^([\w-\.]+)(\@)([a-zA-Z0-9][\w-\.]*[a-zA-Z0-9])(\.)([a-zA-Z0-9]+)$/){
				$newerror = $txt{'14'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}

			foreach $x (@sperre){
				$x =~ s/[\n\r]//g;
				if($x =~ /^\*/){
					$stern = 1;
					($vor,$maili) = split(/\@/,$x);
				}else{
					$stern = 0;
				}

				if(lc($x) eq lc($FORM{$_}) or lc($FORM{$_}) =~ /\@$maili$/i && $stern == 1){
					$newerror = $txt{'15'};
					$newerror =~ s/__1__/$_/g;
					$errormeldung .= $newerror . "\n<br>";
				}
			}
		}
	}

	if($FORM{'space'}){
		foreach (split(/\,/,$FORM{'space'})){
			if($FORM{$_} !~ /^(.+?)\s+(.+?)$/s){
				$newerror = $txt{'16'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($FORM{'urlcheck'}){
		foreach (split /\,/,$FORM{'urlcheck'}){
			if($FORM{$_} !~ /^(http|https)\:\/\/([^"]*)$/){
				$newerror = $txt{'17'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	open(F,"<$internerPfad/mailer-data/sperre-empfaenger.txt");
	flock(F,2) if($flock);
	@sperre2 = <F>;
	flock(F,8) if($flock);
	close(F);

	if(!($empfaenger) && !($FORM{'nextsite'})){
		unless($FORM{'to'}){
			$newerror = $txt{'18'};
			$newerror =~ s/__1__/to/g;
			$errormeldung .= $newerror . "\n<br>";
		}

		foreach (split(/\,/,$FORM{'to'})){
			if($_ !~ /^([\w-\.]+)(\@)([a-zA-Z0-9][\w-\.]*[a-zA-Z0-9])(\.)([a-zA-Z0-9]+)$/){
				$newerror = $txt{'18'};
				$newerror =~ s/__1__/$_/g;
				$errormeldung .= $newerror . "\n<br>";
			}

			foreach $x (@sperre2){
				$x =~ s/[\n\r]//g;
				if($x =~ /^\*/){
					$stern = 1;
					($vor,$maili) = split(/\@/,$x);
				}else{
					$stern = 0;
				}

				if(lc($x) eq lc($_) or lc($_) =~ /\@$maili$/i && $stern == 1){
					$newerror = $txt{'15'};
					$newerror =~ s/__1__/$_/g;
					$errormeldung .= $newerror . "\n<br>";
				}
			}
		}
	}

	$FORM{'from'} = $FORM{'email'} unless($FORM{'from'});
	if(!$FORM{'nextsite'}){
		if(!$FORM{'nofrom'} && $FORM{'from'} !~ /^([\w-\.]+)(\@)([a-zA-Z0-9][\w-\.]*[a-zA-Z0-9])(\.)([a-zA-Z0-9]+)$/ or $FORM{'nofrom'} && $FORM{'from'} && $FORM{'from'} !~ /^([\w-\.]+)(\@)([a-zA-Z0-9][\w-\.]*[a-zA-Z0-9])(\.)([a-zA-Z0-9]+)$/){
#			if($FORM{'from'}){
				$errormeldung .= $txt{'19'} . "\n<br>";
#			}else{
#				$newerror = $txt{'5'};
#				$newerror =~ s/__1__/E-Mail/g;
#				$errormeldung .= $newerror . "\n<br>";
#			}
		}

		foreach (@sperre){
			$_ =~ s/[\n\r]//g;
			if($_ =~ /^\*/){
				$stern = 1;
				($vor,$maili) = split(/\@/,$_);
			}else{
				$stern = 0;
			}

			if(lc($_) eq lc($FORM{'from'}) or lc($FORM{'from'}) =~ /\@$maili$/i && $stern == 1){
				$newerror = $txt{'15'};
				$newerror =~ s/__1__/to/g;
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if($flood == 1 && !$FORM{'nextsite'}){
		foreach (split(/; /,$ENV{'HTTP_COOKIE'})){
			($cookie,$value) = split(/=/);
			$xformmailer = $value if($cookie eq "formmailer");
		}
		$time = time();
		if($time > ($xformmailer+$floodzeit)){
			print "Set-Cookie: formmailer=$time; expires=Mon, 01-Jan-2030 00:00:00 GMT;\n";
		}else{
			$formmailer = $xformmailer;
		}

		$flood = 1;
	        open(F,"+<$internerPfad/mailer-data/flood.txt");
		flock(F,2) if($flock);
		@flood = <F>;
		seek(F,0,0);
		truncate(F,0);
		foreach (@flood){
			$_ =~ s/[\n\r]//g;
			($ipadress,$sekunden) = split(/\|/,$_);
			if($ipadress eq $ENV{'REMOTE_ADDR'}){
				if($time <= ($sekunden+$floodzeit)){
					print F "$ipadress\|$sekunden\n";
					$formmailer = $sekunden;
					$flood = 0;
				}
			}else{
				if($time <= ($sekunden+$floodzeit)){
					print F "$ipadress\|$sekunden\n";
				}
			}
		}
		if($flood == 1){
			print F "$ENV{'REMOTE_ADDR'}\|$time\n";
		}
		flock(F,8) if($flock);
	        close(F);

		if($formmailer){
			$floodzeit = ($formmailer+$floodzeit) - $time;
			if($floodzeit !~ /^\-|^0$/){
				if($floodzeit > 3600){
					$newerror = $txt{'24'};
					$floodzeit = int($floodzeit / 3600);
					$newerror =~ s/__floodzeit__/$floodzeit/g;
				}elsif($floodzeit > 60){
					$newerror = $txt{'23'};
					$floodzeit = int($floodzeit / 60);
					$newerror =~ s/__floodzeit__/$floodzeit/g;
				}else{
					$newerror = $txt{'20'};
					$newerror =~ s/__floodzeit__/$floodzeit/g;
				}
				$errormeldung .= $newerror . "\n<br>";
			}
		}
	}

	if ($TimeZoneOffset ne 0 && $TimeZoneOffset =~ /^\Q-\E/i) {
		$TimeZoneOffset =~ s/[^0-9]//g;
		$Times = time() - ($TimeZoneOffset * 3600);
	}elsif ($TimeZoneOffset ne 0 && $TimeZoneOffset =~ /^\Q+\E/i) {
		$TimeZoneOffset =~ s/[^0-9]//g;
		$Times = time() + ($TimeZoneOffset * 3600);
	}elsif ($TimeZoneOffset ne 0) {
		$TimeZoneOffset =~ s/[^0-9]//g;
		$Times = time() + ($TimeZoneOffset * 3600);
	}else{
		$Times = time();
	}
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($Times);
	$mon_num = $mon+1;
	$hour = "0$hour" if($hour < 10);
	$min = "0$min" if($min < 10);
	$sec = "0$sec" if($sec < 10);
	$year += 1900;

	$mon_num = "0$mon_num" if ($mon_num < 10);
	$mday = "0$mday" if ($mday < 10);

	$thishour = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0) [(localtime)[2]];
	$thismonth = ("Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember")[(localtime)[4]];
	$thisday = (Sonntag,Montag,Dienstag,Mittwoch,Donnerstag,Freitag,Samstag)[(localtime)[6]];

	$aktiv =~ s/<_datum>/\n$FORM{'from'} am $thisday, $mday $thismonth, $year um $hour\:$min\:$sec/g;
	$aktiv =~ s/<_thisday>/$thisday/g;
	$aktiv =~ s/<_thismonth>/$thismonth/g;
	$aktiv =~ s/<_year>/$year/g;
	$aktiv =~ s/<_mday>/$mday/g;
	$aktiv =~ s/<_hour>/$hour/g;
	$aktiv =~ s/<_min>/$min/g;
	$aktiv =~ s/<_sec>/$sec/g;
	$aktiv =~ s/<_ausgabe>/$ausgabe/g;
	$aktiv2 =~ s/<_datum>/\n$FORM{'from'} am $thisday, $mday $thismonth, $year um $hour\:$min\:$sec/g;
	$aktiv2 =~ s/<_thisday>/$thisday/g;
	$aktiv2 =~ s/<_thismonth>/$thismonth/g;
	$aktiv2 =~ s/<_year>/$year/g;
	$aktiv2 =~ s/<_mday>/$mday/g;
	$aktiv2 =~ s/<_hour>/$hour/g;
	$aktiv2 =~ s/<_min>/$min/g;
	$aktiv2 =~ s/<_sec>/$sec/g;
	$aktiv2 =~ s/<_ausgabe>/$ausgabe/g;

	$ENV{'HTTP_X_FORWARDED_FOR'} = $ENV{'HTTP_VIA'} || $ENV{'HTTP_CLIENT_IP'} unless($ENV{'HTTP_X_FORWARDED_FOR'});
	$aktiv =~ s/<_env-proxyip>/$ENV{'HTTP_X_FORWARDED_FOR'}/g;
	$aktiv =~ s/<_env-ip>/$ENV{'REMOTE_ADDR'}/g;
	$aktiv =~ s/<_env-browser>/$ENV{'HTTP_USER_AGENT'}/g;
	$aktiv =~ s/<_env-herkunft>/$ENV{'HTTP_REFERER'}/g;
	$aktiv =~ s/<_env-user>/$ENV{'REMOTE_USER'}/g;
	$aktiv2 =~ s/<_env-proxyip>/$ENV{'HTTP_X_FORWARDED_FOR'}/g;
	$aktiv2 =~ s/<_env-ip>/$ENV{'REMOTE_ADDR'}/g;
	$aktiv2 =~ s/<_env-browser>/$ENV{'HTTP_USER_AGENT'}/g;
	$aktiv2 =~ s/<_env-herkunft>/$ENV{'HTTP_REFERER'}/g;
	$aktiv2 =~ s/<_env-user>/$ENV{'REMOTE_USER'}/g;
	$ende =~ s/<_env-proxyip>/$ENV{'HTTP_X_FORWARDED_FOR'}/g;
	$ende =~ s/<_env-ip>/$ENV{'REMOTE_ADDR'}/g;
	$ende =~ s/<_env-browser>/$ENV{'HTTP_USER_AGENT'}/g;
	$ende =~ s/<_env-herkunft>/$ENV{'HTTP_REFERER'}/g;
	$ende =~ s/<_env-user>/$ENV{'REMOTE_USER'}/g;

	$ausgabe = &txt2html($ausgabe);
	$ausgabe =~ s/\n/<br>/g;
	$ende =~ s/<_datum>/\n$FORM{'from'} am $thisday, $mday $thismonth, $year um $hour\:$min\:$sec/g;
	$ende =~ s/<_thisday>/$thisday/g;
	$ende =~ s/<_thismonth>/$thismonth/g;
	$ende =~ s/<_year>/$year/g;
	$ende =~ s/<_mday>/$mday/g;
	$ende =~ s/<_hour>/$hour/g;
	$ende =~ s/<_min>/$min/g;
	$ende =~ s/<_sec>/$sec/g;
	$ende =~ s/<_ausgabe>/$ausgabe/g;
	$FORM{'to'} = $empfaenger if($empfaenger);
	$ausgabe =~ s/<br>/\n/g;

	$aktiv =~ s/<_subject>/$FORM{'subject'}/g;
	$aktiv2 =~ s/<_subject>/$FORM{'subject'}/g;
	$ende =~ s/<_subject>/$FORM{'subject'}/g;
	$aktiv =~ s/<_from>/$FORM{'from'}/g;
	$aktiv2 =~ s/<_from>/$FORM{'from'}/g;
	$ende =~ s/<_from>/$FORM{'from'}/g;
	$aktiv =~ s/<_to>/$FORM{'to'}/g;
	$aktiv2 =~ s/<_to>/$FORM{'to'}/g;
	$ende =~ s/<_to>/$FORM{'to'}/g;
	$aktiv =~ s/<__subject>/Subject: $FORM{'subject'}/g;
	$aktiv2 =~ s/<__subject>/Subject: $FORM{'subject'}/g;
	$ende =~ s/<__subject>/Subject: $FORM{'subject'}/g;
	$aktiv =~ s/<__from>/From: $FORM{'from'}/g;
	$aktiv2 =~ s/<__from>/From: $FORM{'from'}/g;
	$ende =~ s/<__from>/From: $FORM{'from'}/g;
	$aktiv =~ s/<__to>/To: $FORM{'to'}/g;
	$aktiv2 =~ s/<__to>/To: $FORM{'to'}/g;
	$ende =~ s/<__to>/To: $FORM{'to'}/g;

	if($felderLINE == 1){
		$aktiv =~ s/<_(.+?)>[\n\r]+//sg;
		$aktiv2 =~ s/<_(.+?)>[\n\r]+//sg;
		$aktiv =~ s/<__(.+?)>[\n\r]+//sg;
		$aktiv2 =~ s/<__(.+?)>[\n\r]+//sg;
		$ende =~ s/<_(.+?)>[\n\r]+//sg;
		$ende =~ s/<__(.+?)>[\n\r]+//sg;
	}

	if($felder == 1){
		$aktiv =~ s/<_(.+?)>//g;
		$aktiv2 =~ s/<_(.+?)>//g;
		$aktiv =~ s/<__(.+?)>//g;
		$aktiv2 =~ s/<__(.+?)>//g;
		$ende =~ s/<_(.+?)>//g;
		$ende =~ s/<__(.+?)>//g;
	}
	$boundary = "------------" . &generate_boundary(26) if($anhang == 1);

	@engWochentag = qw(Son Mon Tue Wed Thu Fri Sat);
	@engMonate = qw(&nbsp; Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
	(@datumWert) = localtime(time);
	if($datumWert[5] < 1900){
		$datumWert[5] += 1900;
	}
	$datumWert[4]++;
	if($datumWert[4] < 10){
		$datumWert[4] = "0".$datumWert[4];
	}
	$datumWert[99] = $datumWert[3];
	if($datumWert[3] < 10){
		$datumWert[3] = "0".$datumWert[3];
	}
	if($datumWert[2] < 10){
		$datumWert[2] = "0".$datumWert[2];
	}
	if($datumWert[1] < 10){
		$datumWert[1] = "0".$datumWert[1];
	}
	if($datumWert[0] < 10){
		$datumWert[0] = "0".$datumWert[0];
	}
	$maildatum = $engWochentag[$datumWert[6]].", ".$datumWert[99]." ".$engMonate[$datumWert[4]]." ".$datumWert[5]." ".$datumWert[2].":".$datumWert[1].":".$datumWert[0];
	$maildatum2 = $datumWert[5].$datumWert[4].$datumWert[3].$datumWert[2].$datumWert[1].$datumWert[0];
	$messageID = "<$maildatum2.".&generate_boundary(14)."\@$ENV{HTTP_HOST}>" if($ENV{HTTP_HOST});

	chomp($FORM{'to'});
	chomp($FORM{'from'});
	chomp($FORM{'subject'});

	if($errormeldung){
		&error($errormeldung);
	}

	if($excel){
		if($CSVfrom){
			$kopfcsv .= qq~from$CSVtrennzeichen~;
			$csv .= qq~$FORM{'from'}$CSVtrennzeichen~;
		}
		if($CSVto){
			$kopfcsv .= qq~to$CSVtrennzeichen~;
			$csv .= qq~$FORM{'to'}$CSVtrennzeichen~;
		}
		if($CSVtime){
			$CSVtimestamp =~ s/__tag__/$mday/g;
			$CSVtimestamp =~ s/__monat__/$mon_num/g;
			$CSVtimestamp =~ s/__jahr__/$year/g;
			$CSVtimestamp =~ s/__stunde__/$hour/g;
			$CSVtimestamp =~ s/__minute__/$min/g;
			$CSVtimestamp =~ s/__sekunde__/$sec/g;
			my $timestamp = time;
			$CSVtimestamp =~ s/__timestamp__/$timestamp/g;
			$kopfcsv .= qq~datum$CSVtrennzeichen~;
			$csv .= qq~$CSVtimestamp$CSVtrennzeichen~;
		}
		if($CSVcc){
			$kopfcsv .= qq~cc$CSVtrennzeichen~;
			$csv .= qq~$FORM{'cc'}$CSVtrennzeichen~;
		}
		if($CSVbcc){
			$kopfcsv .= qq~bcc$CSVtrennzeichen~;
			$csv .= qq~$FORM{'bcc'}$CSVtrennzeichen~;
		}
	}

	if($FORM{'csvyes'} != 1){
		if($FORM{'nextsite'} != 1){
			$nextmail .= "From: $FORM{'from'}\n";
			$nextmail .= "Reply-To: $FORM{'from'}\n";
			if($FORM{'cc'}){
				chomp($FORM{'cc'});
				$nextmail .= "Cc: $FORM{'cc'}\n" if(!$empfaenger);
			}
			if($FORM{'bcc'}){
				chomp($FORM{'bcc'});
				$nextmail .= "Bcc: $FORM{'bcc'}\n" if(!$empfaenger);
			}
			$nextmail .= "X-Mailer: Formmailer ($ENV{'HTTP_REFERER'})\n";
			$nextmail .= "Date: $maildatum\n";
			$nextmail .= "Message-ID: $messageID\n";

			if($anhang == 1){
				$nextmail .= "Subject: $FORM{subject}\n";
				$nextmail .= "MIME-Version: 1.0\n";
				$nextmail .= "Content-type: multipart/mixed; boundary=\"$boundary\"\n\n";
				if($FORM{'html'}){
					$nextmail .= "--$boundary\nContent-type: text/html\n\n";
				}else{
					$nextmail .= "--$boundary\nContent-type: text/plain\n\n";
				}
			}else{
				if($FORM{'html'}){
					$nextmail .= "Subject: $FORM{'subject'}\nContent-type: text/html\n\n";
				}else{
					$nextmail .= "Subject: $FORM{'subject'}\nContent-type: text/plain\n\n";
				}
			}
			$nextmail .= "$aktiv\n";

			if($anhang == 1){
				foreach $x (@filenames){
					$nextmail .= "\n--$boundary\n";
					$nextmail .= "Content-type: $MIME{$x};\n" . " name=\"$FILE{$x}\"\n";
					$nextmail .= "Content-Transfer-Encoding: base64\n";
					$nextmail .= "Content-ID: <$FILE{$x}>\n";
					$nextmail .= 'Content-Disposition: attachment;' . " filename=\"$FILE{$x}\"\n\n";
					if($base64){
						$nextmail .= encode_base64($FORM{$x});
					}else{
						$nextmail .= &easyencode_base64($FORM{$x});
					}
				}
				$nextmail .= "\n--$boundary--\n";
			}


			foreach (split(/\,/,$FORM{'to'})){
				if($smtp){
					$smtpOBJECT = Net::SMTP_auth->new($SMTPserver, Timeout => $timeout) or &error("Verbindung zu $SMTPserver konnte nicht aufgebaut werden: $!");
					if($SMTPusername && $SMTPpassword){
						$smtpOBJECT->auth($SMTPtyp,$SMTPusername,$SMTPpassword);
					}

					$smtpOBJECT->mail($ENV{'USER'});
					$smtpOBJECT->to("$_") or &error("Empf&auml;nger wird vom Server nicht akzeptiert: $!");;
					$smtpOBJECT->data();
					$smtpOBJECT->datasend("To: $_\n");
					$smtpOBJECT->datasend($nextmail);
					$smtpOBJECT->dataend();
					$smtpOBJECT->quit();
				}else{
					if($returnpathconfig){
						open (M,"| $mailprog -f $FORM{'from'} -t") or &error("$txt{'22'}");
					}else{
						open (M,"| $mailprog -t") or &error("$txt{'22'}");
					}
					print M "To: $_\n";
					print M $nextmail;
					close(M);
				}
			}
		}
	}

	if($FORM{'csvyes'} != 1 or $FORM{'csvrespond'} == 1){
		if($FORM{'auto'} ne "" && $FORM{'from'} ne "" && $FORM{'nextsite'} != 1){
			if($smtp){
				$smtpOBJECT = Net::SMTP_auth->new($SMTPserver, Timeout => $timeout) or &error("Verbindung(Autoresponder) zu $SMTPserver konnte nicht aufgebaut werden: $!");
				if($SMTPusername && $SMTPpassword){
					$smtpOBJECT->auth($SMTPtyp,$SMTPusername,$SMTPpassword);
				}

				$smtpOBJECT->mail($ENV{'USER'});
				$smtpOBJECT->to("$FORM{'from'}") or &error("Empf&auml;nger(Autoresponder) wird vom Server nicht akzeptiert: $!");;
				$smtpOBJECT->data();
				$smtpOBJECT->datasend("To: $FORM{'from'}\n");
				if($ARabsender){
					$smtpOBJECT->datasend("From: $ARabsender\n");
				}else{
					$smtpOBJECT->datasend("From: $FORM{'to'}\n");
				}
				$smtpOBJECT->datasend("X-Mailer: Formmailer ($ENV{'HTTP_REFERER'})\n");
				$smtpOBJECT->datasend("Date: $maildatum\n");
				$smtpOBJECT->datasend("Message-ID: $messageID\n");
				if($FORM{'htmlresponder'}){
					$smtpOBJECT->datasend("Content-type: text/html\n");
				}else{
					$smtpOBJECT->datasend("Content-type: text/plain\n");
				}
				$smtpOBJECT->datasend($aktiv2);
				$smtpOBJECT->dataend();
				$smtpOBJECT->quit();
			}else{
				if($returnpathconfig){
					open (M,"| $mailprog -f $FORM{'to'} -t") or &error("$txt{'22'}");
				}else{
					open (M,"| $mailprog -t") or &error("$txt{'22'}");
				}
				print M "To: $FORM{'from'}\n";
				if($ARabsender){
					print M "From: $ARabsender\n";
				}else{
					print M "From: $FORM{'to'}\n";
				}
				print M "X-Mailer: Formmailer ($ENV{'HTTP_REFERER'})\n";
				print M "Date: $maildatum\n";
				print M "Message-ID: $messageID\n";
				if($FORM{'htmlresponder'}){
					print M "Content-type: text/html\n";
				}else{
					print M "Content-type: text/plain\n";
				}
				print M $aktiv2;
				close(M);
			}
		}
	}

	$excel = "" if($FORM{'tempv'});
	if($excel && !$nextsite){
		$FORM{'excel'} = $CSVdatei unless($FORM{'excel'});
		$CSVinternerPfad = $internerPfad . "/mailer-data" unless($CSVinternerPfad);
		if(!-e("$CSVinternerPfad/$FORM{'excel'}")){
			if($FORM{'excel'} =~ /^([\w\/-]+)(\.)([\w-]+)$/ && $FORM{'excel'} ne ""){
				open(F,">$CSVinternerPfad/$FORM{'excel'}");
			}else{
				open(F,">$CSVinternerPfad/$CSVdatei");
			}
			if($CSVkopfdaten){
				print F "$kopfcsv$CSVumbruch\n";
			}
			print F "$csv\n";
			close(F);
		}else{
			if($FORM{'excel'} =~ /^([\w\/-]+)(\.)([\w-]+)$/ && $FORM{'excel'} ne ""){
				open(F,">>$CSVinternerPfad/$FORM{'excel'}");
			}else{
				open(F,">>$CSVinternerPfad/$CSVdatei");
			}
			print F "$csv$CSVumbruch";
			close(F);
		}
	}

	if($FORM{'back'} == 1 && $ENV{'HTTP_REFERER'}){
		print "Location: $ENV{'HTTP_REFERER'}\n\n";
		exit;
	}

	$FORM{'next'} = $FORM{'redirect'} unless($FORM{'next'});
	$FORM{'next'} = $FORM{'fertig'} if(!$FORM{'next'} && $FORM{'fertig'} =~ /^http:\/\//i);
	if($FORM{'next'}){
		$FORM{'next'} =~ s/http:/https:/ig if($ENV{'HTTPS'});
		print "Location: $FORM{'next'}\n\n";
		exit;
	}
	&ausgabe($ende);
}

sub ausgabe {
	local($html) = @_;

	if($lwpsimple == 1){
		$html =~ s/<!--INCLUDE-->(.+?)<!--INCLUDE-->/&lwpsimple($1)/eg;
	}else{
		$html =~ s/<!--INCLUDE-->(.+?)<!--INCLUDE-->//g;
	}

	if($ENV{'HTTP_ACCEPT_ENCODING'} =~ /(x-gzip|gzip)/ && $ENV{'SERVER_PROTOCOL'} eq "HTTP/1.1" && $gzip == 1){
		print "Content-Encoding: $1\n";
		print "Content-Type: text/html\n\n";
		binmode STDOUT;
		if($zlib){
			print Compress::Zlib::memGzip($html);
		}else{
			open(GZIP, "| gzip -f");
			binmode(GZIP);
			print GZIP $html;
			close(GZIP);
		}
	}else{
		print "Content-Type: text/html\n\n";
		print $html;
	}

	exit;
}

sub check {
	if($offline == 1){
		local($check_referer) = 0;
		if($ENV{'HTTP_REFERER'}){
			open(F,"<$internerPfad/mailer-data/domains.txt");
			flock(F,2) if($flock);
			foreach $r (<F>){
				$r =~ s/[\n\r]//g;
				if($ENV{'HTTP_REFERER'} =~ m|https?://([^/]*)$r|i){
					$check_referer = 1;
					last;
				}
			}
			flock(F,8) if($flock);
			close(F);
		}else{
			$check_referer = 0;
		}
		if($check_referer != 1){
			&error("$txt{'21'}");
		}
	}
}

sub generate_boundary() {
	my ($boundary, @boundaryv, $i);
	@boundaryv = (0..9, 'A'..'F');
	for ($i = 0; $i++ < $_[0];) {
		$boundary .= $boundaryv[rand(@boundaryv)];
	}
	return $boundary;
}

sub easyencode_base64 (){
	my $res = "";

	while ($_[0] =~ /(.{1,45})/gs) {
		$res .= substr(pack('u', $1), 1);
		chop($res);
	}
	$res =~ tr|` -_|AA-Za-z0-9+/|;
	my $padding = (3 - length($_[0]) % 3) % 3;
	$res =~ s/.{$padding}$/'=' x $padding/e if $padding;

	$res =~ s/(.{1,76})/$1\n/g;
	return $res;
}


sub easydecode_base64 (){
	my $str = shift;
	my $res = "";

	$str =~ tr|A-Za-z0-9+=/||cd;
	exit if(length($str) % 4); # Länge der Daten "Base64" kann nicht mit 4 multipliziert werden.
	$str =~ s/=+$//;
	$str =~ tr|A-Za-z0-9+/| -_|;
	while ($str =~ /(.{1,60})/gs) {
		my $len = chr(32 + length($1)*3/4);
		$res .= unpack("u", $len . $1 );
	}
	return $res;
}

sub txt2html {
	local($text) = @_;
	$text =~ s/\"/&quot;/g;
	$text =~ s!&lt;!&#60;!g;
	$text =~ s!&gt;!&#62;!g;
	$text =~ s/>/&gt;/g;
	$text =~ s/</&lt;/g;
	$text =~ s/ä/&auml;/g;
	$text =~ s/ö/&ouml;/g;
	$text =~ s/ü/&uuml;/g;
	$text =~ s/Ä/&Auml;/g;
	$text =~ s/Ö/&Ouml;/g;
	$text =~ s/Ü/&Uuml;/g;
	$text =~ s/ß/&szlig;/g;
	$text =~ s/\|/\&\#124\;/g;
#        $text =~ s/_/&#095;/g;
	return $text;
}

sub html2txt {
	local($text) = @_;
	$text =~ s/&quot;/\"/g;
	$text =~ s/&gt;/>/g;
	$text =~ s/&lt;/</g;
	$text =~ s!&#60;!&lt;!g;
	$text =~ s!&#62;!&gt;!g;
	$text =~ s/&auml;/ä/g;
	$text =~ s/&ouml;/ö/g;
	$text =~ s/&uuml;/ü/g;
	$text =~ s/&Auml;/Ä/g;
	$text =~ s/&Ouml;/Ö/g;
	$text =~ s/&Uuml;/Ü/g;
	$text =~ s/&szlig;/ß/g;
	$text =~ s/\&\#124\;/\|/g;
#        $text =~ s/&#095;/_/g;
	return $text;
}

sub rechnen ($) {
	local($e) = shift;
	$e =~ s/\[(.+?)\]/rechnenzahl($FORM{$1})/g;
	eval {
		local $SIG{ALRM} = sub { die "alarm\n" };
		alarm(5);
		$ergebnis = eval $e;
		alarm(0);
	};
	return sprintf("%.2f",$ergebnis);
}

sub rechnenzahl ($) {
	local($e) = shift;
	$e =~ s/[^\d]//g;
	return($e);
}

sub all_options {
   my %gd = (
   gd_ttf => {
      width      => 220,
      height     => 90,
      send_ctobg => 1,
      font       => $config{font},
      ptsize     => 30,
   },
   gd_ttf_scramble =>  {
      width      => 360,
      height     => 100,
      send_ctobg => 1,
      font       => $config{font},
      ptsize     => 25,
      scramble   => 1,
   },
   gd_ttf_scramble_fixed =>  {
      width      => 360,
      height     => 80,
      send_ctobg => 1,
      font       => $config{font},
      ptsize     => 25,
      scramble   => 1,
      angle      => 30,
   },
   );
   my %magick = (
   magick => {
      width      => 250,
      height     => 100,
      send_ctobg => 1,
      font       => $config{font},
      ptsize     => 50,
   },
   magick_scramble => {
      width      => 350,
      height     => 100,
      send_ctobg => 1,
      font       => $config{font},
      ptsize     => 30,
      scramble   => 1,
   },
   magick_scramble_fixed => {
      width      => 350,
      height     => 80,
      send_ctobg => 1,
      font       => $config{font},
      ptsize     => 30,
      scramble   => 1,
      angle      => 32,
   },
   );
   return $IS_GD ? (%gd) : (%magick);
}

sub all_styles {
   ec => {
      name       => 'ec',
      lines      => 16,
      bgcolor    => [ 0,   0,   0],
      text_color => [84, 207, 112],
      line_color => [ 0,   0,   0],
      particle   => 1000,
   },
   ellipse => {
      name       => 'ellipse',
      lines      => 15, 
      bgcolor    => [208, 202, 206],
      text_color => [184,  20, 180],
      line_color => [184,  20, 180],
      particle   => 2000,
   },
   circle => {
      name       => 'circle',
      lines      => 40, 
      bgcolor    => [210, 215, 196],
      text_color => [ 63, 143, 167], 
      line_color => [210, 215, 196],
      particle   => 3500,
   },
   box => {
      name       => 'box',
      lines      => 6,
      text_color => [245, 240, 220],
      line_color => [115, 115, 115],
      particle   => 3000,
      dots       => 2,
   },
   rect => {
      name       => 'rect',
      lines      => 30,
      text_color => [ 63, 143, 167], 
      line_color => [226, 223, 169],
      particle   => 2000,
   },
   default => {
      name       => 'default',
      lines      => 10,
      text_color => [ 68, 150, 125],
      line_color => [255,   0,   0],
      particle   => 5000,
   },
}

sub refresh2 {
	%config = (font       => './GD/comic.ttf');
	GD::SecurityImage->import(use_magick => $magick);

	$IS_GD           = $GD::SecurityImage::BACKEND eq 'GD';
	%options      = &all_options();
	%styles       = &all_styles();
	@optz         = keys %options;
	@styz         = keys %styles;
	$rnd_opt = $options{$optz[int rand @optz]};
	$rnd_sty = $styles{ $styz[int rand @styz]};

	   $image     = GD::SecurityImage->new(
	      lines   => $rnd_sty->{lines},
	      bgcolor => $rnd_sty->{bgcolor},
	      width => $rnd_opt->{width},
	      height => $rnd_opt->{height},
	      font => $rnd_opt->{font},
	      ptsize => $rnd_opt->{ptsize},
	      ptsize => $rnd_opt->{ptsize},
	      scramble => $rnd_opt->{scramble},
	      angle => $rnd_opt->{angle},
	      send_ctobg => $rnd_opt->{send_ctobg},
	   );
	$image->random(String::Random->new->randregex('\g\g\g\g\g\g'));
	$random_numberx = $image->random_str();
	$image->create(ttf => $rnd_sty->{name}, $rnd_sty->{text_color}, $rnd_sty->{line_color});
	$image->particle($rnd_sty->{dots} ? ($rnd_sty->{particle}, $rnd_sty->{dots}) : ($rnd_sty->{particle}));
	my($image_data, $mime_type, $random_number) = $image->out(force => 'png');;

	$Times = time();
	open(F,"+<mailer-data/sessiongrafik.txt");
	flock(F,2) if($flock);
	@session = <F>;
	seek(F,0,0);
	truncate(F,0);
	foreach(@session){
		s/[\n\r]//g;
		($SESSIONkey,$SESSIONtime) = split(/\|/);
		if($Times < ($SESSIONtime+3600)){
			print F $_ . "\n";
		}
	}
	print F "$random_number\|$Times\n";
	flock(F,8) if($flock);
	close(F);

	print "Content-Type: image/png\n\n";
	print $image_data;
	exit;
}

sub lwpsimple ($){
	return get($_[0]);
}
