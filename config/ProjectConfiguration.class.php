<?php

require_once '/www/symfony/lib/autoload/sfCoreAutoload.class.php';
sfCoreAutoload::register();

class ProjectConfiguration extends sfProjectConfiguration{

  public function setup(){
    //Enable Zend Component For sfDoctrineApplyPlugin
    set_include_path(sfConfig::get('sf_lib_dir') . '/vendor' . PATH_SEPARATOR . get_include_path());

    $this->enablePlugins('sfDoctrinePlugin');

    //Enable User Management Plugins
    $this->enablePlugins('sfDoctrineGuardPlugin');
    $this->enablePlugins('sfDoctrineApplyPlugin');

    //Add Some Behavior To Doctrine
    $this->enablePlugins('csDoctrineActAsSortablePlugin');
    $this->enablePlugins('sfDoctrineActAsSignablePlugin');
    
    $this->enablePlugins('sfProjectAnalyserPlugin');
  }

}
