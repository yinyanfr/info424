package generateur;

import java.io.*;
import java.util.Scanner;

public class LireSurEntreeStandard {

	/**
	 * Démonstration simplissible de lecture ligne par ligne sur l'entrée standard.
	 */
	public static void main (String[] args) {
		// On ouvre l'entrée standard
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// uneLigne va stocker la ligne lue
		String uneLigne = null;
		// continuer indique s'il y a encore des choses à lire ou si on a terminé.
		boolean continuer = true;
		while ( continuer ) {
			try {
				uneLigne = br.readLine();
				if ( uneLigne != null ) {
					// On affiche chaque ligne lue
					System.out.println( "-->" + uneLigne + "<--" );
					// on supprime les espaces multiples
					uneLigne.replaceAll( "\\s+", " " ); 
					// On va maintenant la réafficher en séparant les mots.
					System.out.print( "|" );
					for ( String s : uneLigne.split( " " ) ) {
						if ( s.length() > 0 ) {
							System.out.print( s + "|" );
						}
					}
					System.out.println( "" );
				} else {
					continuer = false;
				}
			} catch (IOException ioe) {
				System.out.println( "Erreur de lecture" );
				System.exit(1);
			}
		}
	}
}  

