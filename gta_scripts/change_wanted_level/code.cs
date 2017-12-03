using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using GTA;
using GTA.Native;
using GTA.Math;

namespace ScriptChangeWantedLevel
{
    public class Class1 : Script
    {
        public Class1()
        {
            Tick += onTick;
            KeyDown += onKeyDown;
        }

        private void onTick(object sender, EventArgs e)
        {

        }

        private void onKeyDown(object sender, KeyEventArgs e)
        {
            // Remove one star
            if (e.KeyCode == Keys.O)
            {
                if (Game.Player.WantedLevel > 0)
                {
                    Game.Player.WantedLevel -= 1;
                    UI.ShowSubtitle("Substracted one wanted level");
                }
            }

            // Add one star
            if (e.KeyCode == Keys.H)
            {
                if (Game.Player.WantedLevel < 5)
                {
                    Game.Player.WantedLevel += 1;
                    UI.ShowSubtitle("Added one wanted level");
                }
            }


            /*
            // Remove one star
            if (e.KeyCode == Keys.Subtract && Game.Player.WantedLevel > 0)
            {
                Game.Player.WantedLevel -= 1;
                UI.ShowSubtitle("Substracted one wanted level");
            }

            // Add one star
            if (e.KeyCode == Keys.Add && Game.Player.WantedLevel < 5)
            {
                Game.Player.WantedLevel += 1;
                UI.ShowSubtitle("Added one wanted level");
            }
            */
        }
    }
}
