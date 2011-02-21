<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of sfGuardRegisterForm
 *
 * @author JS
 */
class sfGuardRegisterForm extends sfGuardUserForm
{
  public function configure()
  {
    parent::configure();
    $this->validatorSchema['password'] = new sfValidatorString(
      array('min_length' => 6, 'max_length' => 128)
    );
  }
}