local wezterm = require("wezterm")
local theme = require("lua/rose-pine").main

-- Event handler to maximize on startup
wezterm.on('gui-startup', function(cmd)
  local tab, pane, window = wezterm.mux.spawn_window(cmd or {})
  window:gui_window():maximize()
end)

return {
  colors = theme.colors(),
  window_frame = theme.window_frame(),
  enable_tab_bar = false,
  default_prog = { "tmux" },
  window_decorations = "TITLE | RESIZE",
}
