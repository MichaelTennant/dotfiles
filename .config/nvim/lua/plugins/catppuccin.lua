return {
    "catppuccin/nvim", 
    name = "catppuccin", 
    priority = 1000, 
    config = function(LazyPlugin, opts)
        vim.cmd.colorscheme "catppuccin-macchiato"
    end
}
