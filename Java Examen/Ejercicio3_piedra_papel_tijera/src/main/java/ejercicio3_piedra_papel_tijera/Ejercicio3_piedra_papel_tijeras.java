/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package ejercicio3_piedra_papel_tijera;

import java.util.Random;
import javax.swing.JOptionPane;
/**
 *
 * @author elton
 */
public class Ejercicio3_piedra_papel_tijeras extends javax.swing.JFrame {
    private int cpuvic = 0;
    private int jugavic = 0;
    private int empate = 0;
    /**
     * Creates new form Ejercicio3_piedra_papel_tijeras
     */
    public Ejercicio3_piedra_papel_tijeras() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        salir = new javax.swing.JRadioButton();
        piedra = new javax.swing.JRadioButton();
        papel = new javax.swing.JRadioButton();
        resultado = new javax.swing.JTextField();
        tijera = new javax.swing.JRadioButton();
        mostrar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        salir.setText("Salir.");
        salir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                salirActionPerformed(evt);
            }
        });

        buttonGroup1.add(piedra);
        piedra.setText("Piedra");
        piedra.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                piedraMouseClicked(evt);
            }
        });
        piedra.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                piedraActionPerformed(evt);
            }
        });

        buttonGroup1.add(papel);
        papel.setText("Papel");
        papel.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                papelActionPerformed(evt);
            }
        });

        resultado.setEditable(false);
        resultado.setText("Resultado:");
        resultado.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                resultadoActionPerformed(evt);
            }
        });

        buttonGroup1.add(tijera);
        tijera.setText("Tijera");
        tijera.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                tijeraActionPerformed(evt);
            }
        });

        mostrar.setText("Mostrar");
        mostrar.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                mostrarMouseClicked(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(salir)
                            .addComponent(piedra, javax.swing.GroupLayout.PREFERRED_SIZE, 216, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(tijera, javax.swing.GroupLayout.PREFERRED_SIZE, 216, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(papel)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(116, 116, 116)
                                .addComponent(mostrar))))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(18, 18, 18)
                        .addComponent(resultado, javax.swing.GroupLayout.PREFERRED_SIZE, 350, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(32, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(35, 35, 35)
                .addComponent(piedra)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(papel)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(tijera)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(salir)
                .addGap(36, 36, 36)
                .addComponent(mostrar)
                .addGap(42, 42, 42)
                .addComponent(resultado, javax.swing.GroupLayout.PREFERRED_SIZE, 31, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(29, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void salirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_salirActionPerformed

        System.exit(0); // Termina el programa

    }//GEN-LAST:event_salirActionPerformed


    private void piedraMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_piedraMouseClicked
        // TODO add your handling code here:

    }//GEN-LAST:event_piedraMouseClicked

    private void piedraActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_piedraActionPerformed

    }//GEN-LAST:event_piedraActionPerformed

    private void papelActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_papelActionPerformed

    }//GEN-LAST:event_papelActionPerformed

    private void resultadoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_resultadoActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_resultadoActionPerformed

    private void tijeraActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_tijeraActionPerformed

    }//GEN-LAST:event_tijeraActionPerformed

    private void mostrarMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_mostrarMouseClicked
    try {
            Random random = new Random();
            int cpu = random.nextInt(3) + 1;

            if (piedra.isSelected()) {
                if (cpu == 1) {
                    resultado.setText("Jugador: piedra. CPU: piedra, resultado: empate");
                    empate++;
                } else if (cpu == 2) {
                    resultado.setText("Jugador: piedra. CPU: papel, resultado: gana la CPU");
                    cpuvic++;
                } else {
                    resultado.setText("Jugador: piedra. CPU: tijera, resultado: gana el jugador");
                    jugavic++;
                }
            } else if (papel.isSelected()) {
                if (cpu == 1) {
                    resultado.setText("Jugador: papel. CPU: piedra, resultado: gana el jugador");
                    jugavic++;
                } else if (cpu == 2) {
                    resultado.setText("Jugador: papel. CPU: papel, resultado: empate");
                    empate++;
                } else {
                    resultado.setText("Jugador: papel. CPU: tijera, resultado: gana la CPU");
                    cpuvic++;
                }
            } else if (tijera.isSelected()) {
                if (cpu == 1) {
                    resultado.setText("Jugador: tijera. CPU: piedra, resultado: gana la CPU");
                    cpuvic++;
                } else if (cpu == 2) {
                    resultado.setText("Jugador: tijera. CPU: papel, resultado: gana el jugador");
                    jugavic++;
                } else {
                    resultado.setText("Jugador: tijera. CPU: tijera, resultado: empate");
                    empate++;
                }
            } else {
                JOptionPane.showMessageDialog(this, "Seleccione una opción (Piedra, Papel o Tijera).");
            }
            
            // Actualiza el texto para mostrar el resultado acumulado
            resultado.setText("Victorias del jugador: " + jugavic + " / Empates: " + empate + " / Victorias de la CPU: " + cpuvic);

        } catch (NumberFormatException e) {
            resultado.setText("ERROR: Valor inválido.");
        }
    }//GEN-LAST:event_mostrarMouseClicked

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Ejercicio3_piedra_papel_tijeras.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Ejercicio3_piedra_papel_tijeras.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Ejercicio3_piedra_papel_tijeras.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Ejercicio3_piedra_papel_tijeras.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Ejercicio3_piedra_papel_tijeras().setVisible(true);
            }
        });
    }
    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JButton mostrar;
    private javax.swing.JRadioButton papel;
    private javax.swing.JRadioButton piedra;
    private javax.swing.JTextField resultado;
    private javax.swing.JRadioButton salir;
    private javax.swing.JRadioButton tijera;
    // End of variables declaration//GEN-END:variables
}
